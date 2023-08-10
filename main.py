from linkedin import Linkedin
import csv

job_title = "python developer"
def main():
    link = Linkedin()
    # search job with given titles
    link.search_job(title=job_title)
    # get jobs details from searched jobs
    jobs = link.jobs_processing()
    if jobs is not None:
        link.quit()
        with open('job_details.csv', 'w') as file:

            data = csv.DictWriter(file, jobs.keys())
            data.writeheader()
            data.writerow(jobs)


if __name__ == '__main__':
    main()

