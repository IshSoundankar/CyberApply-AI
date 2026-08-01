import { useEffect, useState } from "react";

import { getTopJobs } from "../api/jobs";

import JobCard from "../components/JobCard";


function Dashboard() {

    const [jobs, setJobs] = useState([]);


    useEffect(() => {

        async function loadJobs() {

            try {

                const data = await getTopJobs();

                setJobs(data);

            } catch (error) {

                console.error(
                    "Failed loading jobs:",
                    error
                );

            }

        }


        loadJobs();

    }, []);



    return (

        <div>

            <h1>
                CyberApply Dashboard
            </h1>


            {
                jobs.map((job) => (

                    <JobCard
                        key={job.id}
                        job={job}
                    />

                ))
            }


        </div>

    );

}


export default Dashboard;