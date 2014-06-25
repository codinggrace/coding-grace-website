# This is reading .md files and saving them to django
import glob
import os

from django.core.management.base import BaseCommand, CommandError
from django.utils.text import slugify

from events.models import Chapter, City, Country, Event, Location, Organiser
from news.models import NewsPost

import iso8601

class Command(BaseCommand):
    help = 'Once off moving markdown posts and save to django'

    def add_arguments(self, parser):
        parser.add_argument('md_files_path', nargs='+', type=str)

    def handle(self, *args, **options):
        # Get current working directory and the md file paths given when command is run
        cwd = os.getcwd()
        md_files_path = os.path.join(cwd, args[0])

        # Retrieve all the .md files found in the given directory
        md_files = glob.glob("{}/*.md".format(md_files_path))

        # Result
        # [{title:"", published:"", author:"", description:""}, {title:"", published:"", author:"", description:""}]
        md_posts = []
        md_post_dict = {}
        for md_file in md_files:
            count = 0
            with open(md_file, "r") as f:
                # First four lines are meta data
                while count < 4:
                    meta_data = f.readline().split(": ")[1].strip()
                    if count == 0:
                        title = meta_data
                        md_post_dict["title"] = meta_data
                    elif count == 1:
                        published = iso8601.parse_date(meta_data)
                        md_post_dict["published"] = meta_data
                    elif count == 2:
                        tags = meta_data
                        md_post_dict["tags"] = meta_data
                    elif count == 3:
                        author = meta_data
                        md_post_dict["author"] = meta_data
                    count += 1
                rest = f.read()
                md_post_dict["content"] = rest
            md_posts.append(md_post_dict)

            md_news = NewsPost( title = title,
                                published = published,
                                author = Organiser.objects.get(pk=1),
                                chapter = Chapter.objects.get(pk=1),
                                slug = slugify(title),
                                short_description = rest[:350],
                                content = rest
                                )
            md_news.save()




# def main():
#     # Getting the list of md files
#     cwd = os.getcwd()
#     md_files = glob.glob("{}/*.md".format(cwd))

#     md_file_dict = {}

#     for md_file in md_files:
#         count = 0
#         with open(md_file, "r") as f:
#             while count < 4:
#                 if count == 0:
#                     title = f.readline().split(": ")[1]
#                 elif count == 1:
#                     published = f.readline().split(": ")[1]
#                 elif count == 2:
#                     tags = f.readline().split(": ")[1]
#                 elif count == 3:
#                     author = f.readline().split(": ")[1]
#                 count += 1
#             rest = f.read()

#             # title, level_type,





# if __name__ == '__main__':
#     main()