
class TemplateGen:

    def __init__(self):
      pass

    def generate_db(self):
      my_string = """
      [database]
      host = localhost
      port = 5432
      database = custom_rails_development
      username = "patcasrares"
      password = ""

      """

      with open("myfile.txt", "w") as f:
          f.write(my_string)
