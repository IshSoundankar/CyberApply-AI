function JobCard({ job }) {

    return (
        <div className="job-card">

            <h2>{job.title}</h2>

            <h3>{job.company}</h3>

            <p>
                Location: {job.location}
            </p>

            <p>
                CV: {job.cv_type}
            </p>

            <p>
                Match Score: {job.ai_score}
            </p>

            <p>
                Status: {job.status}
            </p>


            <a
                href={job.url}
                target="_blank"
                rel="noreferrer"
            >
                View Job
            </a>

        </div>
    );
}


export default JobCard;