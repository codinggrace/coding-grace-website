job "codinggrace" {
	datacenters = ["scaleway"]

	update {
		stagger = "10s"
		max_parallel = 1
	}

	group "memcached" {
		count = 1

		ephemeral_disk {
			size = 200
		}

		task "memcached" {
			driver = "docker"
			config {
				image = "memcached:latest"
				port_map {
					memcached = 11211
				}
			}
			service {
				name = "codinggrace-memcached"
				port = "memcached"
				check {
					name = "alive"
					type = "tcp"
					interval = "10s"
					timeout = "2s"
				}
			}
			resources {
				cpu = 500
				memory = 64
				network {
					mbits = 10
					port "memcached" {}
				}
			}
		}
	}

	group "postgresql" {
		count = 1

		ephemeral_disk {
			size = 500
			migrate = true
			sticky = true
		}

		task "postgresql" {
			driver = "docker"
			config {
				image = "gitlab.twomeylee.name:7443/twomeylee/postgresql:9.5.5-1"
                command = "/bin/bash"
                args = ["${NOMAD_TASK_DIR}/run.sh"]
				port_map {
					psql = 5432
				}
			}
			service {
				name = "codinggrace-postgresql"
				port = "psql"
				check {
					type = "script"
					name = "pg_isready"
					command = "/usr/bin/pg_isready"
					interval = "10s"
					timeout = "2s"
				}
			}
			resources {
				cpu = 500
				memory = 64
				network {
					mbits = 10
					port "psql" {}
				}
			}

            template {
                destination = "${NOMAD_TASK_DIR}/run.sh"
                data = <<<EOF
#!/bin/bash
export POSTGRES_DB="{{key "codinggrace/prod/postgresql/db"}}"
export POSTGRES_USER="{{key "codinggrace/prod/postgresql/user"}}"
export POSTGRES_PASSWORD="{{key "codinggrace/prod/postgresql/password"}}"
export AWS_ACCESS_KEY_ID="{{key "postgresql-backups/aws_access_key_id"}}"
export AWS_SECRET_ACCESS_KEY="{{key "postgresql-backups/aws_secret_access_key"}}"
export S3_BUCKET="{{key "postgresql-backups/bucket"}}"
export S3_PREFIX="codinggrace/"

exec /usr/local/bin/run.sh
EOF
            }
		}
	}

	group "app" {
		count = 3

		ephemeral_disk {
			size = 200
		}

		restart {
			attempts = 10
			interval = "5m"
			delay = "25s"
			mode = "delay"
		}

		task "codinggrace" {
			driver = "docker"

			config {
				image = "{{env "TAG"}}"
                command = "/bin/bash"
                args = ["${NOMAD_TASK_DIR}/run.sh"]
				port_map {
					http = 8000
				}
			}

			service {
				name = "codinggrace"
				tags = [
					"codinggrace",
					"http",
					"urlprefix-codinggrace.twomeylee.name/",
					"urlprefix-codinggrace.com/",
					"urlprefix-www.codinggrace.com/"
				]
				port = "http"
				check {
					name = "health"
					type = "http"
					path = "/"
					interval = "10s"
					timeout = "2s"
				}
				check {
					name = "alive"
					type = "tcp"
					interval = "10s"
					timeout = "2s"
				}
			}

			resources {
				cpu = 500
				memory = 256
				network {
					mbits = 10
					port "http" {
					}
				}
			}

			template {
                destination = "${NOMAD_TASK_DIR}/run.sh"
                data = <<<EOF
#!/bin/bash
{{if service "codinggrace-postgresql@scaleway"}}
{{with index (service "codinggrace-postgresql@scaleway") 0}}
export POSTGRESQL_HOST="{{.Address}}"
export POSTGRES_PORT="{{.Port}}"
export DATABASE_URL="postgres://{{key "codinggrace/prod/postgresql/user"}}:{{key "codinggrace/prod/postgresql/password"}}@{{.Address}}:{{.Port}}/{{key "codinggrace/prod/postgresql/db"}}"
{{end}}
{{end}}

export POSTGRESQL_DB="{{key "codinggrace/prod/postgresql/db"}}"
export POSTGRESQL_USER="{{key "codinggrace/prod/postgresql/user"}}"
export POSTGRESQL_PASSWORD="{{key "codinggrace/prod/postgresql/password"}}"

export MEMCACHIER_USERNAME="{{key "codinggrace/prod/memcached/username"}}"
export MEMCACHIER_PASSWORD="{{key "codinggrace/prod/memcached/password"}}"
export MEMCACHIER_SERVERS="{{key "codinggrace/prod/memcached/host"}}:{{key "codinggrace/prod/memcached/port"}}"

export DJANGO_SECRET_KEY="{{key "codinggrace/prod/django_secret_key"}}"
export HOSTEDGRAPHITE_APIKEY="{{key "codinggrace/prod/hostedgraphite_apikey"}}"

exec gunicorn codinggrace_django.wsgi --bind 0.0.0.0:8000 --log-file=-
EOF
			}
		}
	}
}
