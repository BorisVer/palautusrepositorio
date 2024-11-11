from urllib import request
from project import Project
import toml


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        toml_content = toml.loads(content)
        name = toml_content["tool"]["poetry"]["name"]
        description = toml_content["tool"]["poetry"]["description"]

        dependencies = toml_content["tool"]["poetry"]["dependencies"]
        all_dependencies = ""
        for i in dependencies:
            all_dependencies += "- " + i + " \n"
        development_dependencies = toml_content["tool"]["poetry"]["group"]["dev"]["dependencies"]
        all_development_dependencies = ""
        for i in development_dependencies:
            all_development_dependencies += "- " + i + " \n"

        license = toml_content["tool"]["poetry"]["license"]
        authors = toml_content["tool"]["poetry"]["authors"]
        all_authors = ""
        for i in authors:
            all_authors += "- " + i + " \n"

        print("Name: " + name)
        print("Description: " + description)
        print("License: " + license + "\n")
        print("Authors: \n" + all_authors)
        print("Dependencies: " + all_dependencies)
        print("Development Dependencies: " + all_development_dependencies)


        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project("Test name", "Test description", [], [])
