from linkedin import Linkedin


def main():
    link = Linkedin()
    link.search_job(title="python developer")
    link.jobs_processing()


if __name__ == '__main__':
    main()

