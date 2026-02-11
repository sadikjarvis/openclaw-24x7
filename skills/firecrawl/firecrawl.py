class FireCrawl:
    name = "FireCrawl"
    description = "Searches, fetches info and runs tasks automatically"

    def run(self, prompt):
        from openclaw import gpt_oss_20b
        return gpt_oss_20b(prompt)
