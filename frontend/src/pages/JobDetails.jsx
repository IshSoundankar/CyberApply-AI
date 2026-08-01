import { useEffect, useState } from "react";

import {
    useParams
} from "react-router-dom";

import axios from "axios";



function JobDetails() {


    const { id } = useParams();


    const [job, setJob] = useState(null);




    useEffect(() => {


        axios.get(

            `http://127.0.0.1:8000/jobs/${id}`

        )

        .then(response => {


            setJob(
                response.data
            );


        })


        .catch(error => {


            console.error(
                error
            );


        });



    }, [id]);






    if (!job) {


        return (

            <div className="job-details">

                Loading...

            </div>

        );

    }







    return (


        <div className="job-details">



            <h1>

                {job.title}

            </h1>




            <h3>

                {job.company}

            </h3>




            <p>

                Location:
                {" "}
                {job.location}

            </p>




            <p>

                CV:
                {" "}
                {job.cv_type}

            </p>




            <p>

                Match Score:
                {" "}
                {job.ai_score}

            </p>




            <p>

                Status:
                {" "}
                {job.status}

            </p>





            <hr />




            <h2>

                Description

            </h2>




            <p>

                {job.description}

            </p>






            <a

                href={job.url}

                target="_blank"

                rel="noreferrer"

            >



                <button className="view-button">

                    Apply

                </button>



            </a>




        </div>


    );

}



export default JobDetails;