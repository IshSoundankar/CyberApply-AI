import "./App.css";

import { useEffect, useState } from "react";

import {
  getTopJobs,
  updateJobStatus
} from "./api/jobs";



function App() {


  const [jobs, setJobs] = useState([]);

  const [search, setSearch] = useState("");

  const [filter, setFilter] = useState("ALL");




  useEffect(() => {


    getTopJobs()

      .then(data => {

        setJobs(data);

      })

      .catch(error => {

        console.error(
          "Error loading jobs:",
          error
        );

      });


  }, []);






  async function changeStatus(
    id,
    status
  ) {


    try {


      await updateJobStatus(
        id,
        status
      );



      setJobs(

        jobs.map(job =>

          job.id === id

          ?

          {
            ...job,
            status: status
          }

          :

          job

        )

      );


    }

    catch(error) {


      console.error(
        "Status update failed:",
        error
      );


    }

  }






  const totalJobs = jobs.length;


  const savedJobs = jobs.filter(
    job => job.status === "SAVED"
  ).length;



  const appliedJobs = jobs.filter(
    job => job.status === "APPLIED"
  ).length;



  const rejectedJobs = jobs.filter(
    job => job.status === "REJECTED"
  ).length;







  const filteredJobs = jobs.filter(job => {


    const text = (

      job.title +

      job.company +

      job.cv_type

    ).toLowerCase();




    const matchesSearch =

      text.includes(
        search.toLowerCase()
      );




    const matchesFilter =

      filter === "ALL" ||

      job.cv_type === filter;




    return (

      matchesSearch &&

      matchesFilter

    );


  });







  return (


    <div className="dashboard">



      <div className="header">

        CyberApply Dashboard

      </div>






      <div className="stats">



        <div className="stat-card">

          Total Jobs

          <strong>
            {totalJobs}
          </strong>

        </div>





        <div className="stat-card">

          Saved

          <strong>
            {savedJobs}
          </strong>

        </div>





        <div className="stat-card">

          Applied

          <strong>
            {appliedJobs}
          </strong>

        </div>





        <div className="stat-card">

          Rejected

          <strong>
            {rejectedJobs}
          </strong>

        </div>



      </div>







      <div className="controls">



        <input

          type="text"

          placeholder="Search jobs..."

          value={search}

          onChange={
            (e)=>
            setSearch(e.target.value)
          }

        />





        <select

          value={filter}

          onChange={
            (e)=>
            setFilter(e.target.value)
          }

        >


          <option value="ALL">
            All
          </option>



          <option value="Blue Team">
            Blue Team
          </option>



          <option value="Network Security">
            Network Security
          </option>



          <option value="Security Engineering">
            Security Engineering
          </option>



        </select>



      </div>








      <div className="jobs-container">



        {filteredJobs.map(job => (



          <div

            className="job-card"

            key={job.id}

          >




            <h2>

              {job.title}

            </h2>





            <p>

              <b>
                {job.company}
              </b>

            </p>





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





            <span className="score">

              Match Score:
              {" "}
              {job.ai_score}

            </span>






            <br />






            <label>

              Status:

            </label>





            <select


              className={
                `status-${job.status.toLowerCase()}`
              }


              value={job.status}


              onChange={
                (e)=>
                changeStatus(
                  job.id,
                  e.target.value
                )
              }


            >



              <option value="NEW">

                NEW

              </option>



              <option value="SAVED">

                SAVED

              </option>



              <option value="APPLIED">

                APPLIED

              </option>



              <option value="REJECTED">

                REJECTED

              </option>



            </select>







            <br />






            <a href={`/job/${job.id}`}>

            <button className="view-button">

            View Job

            </button>

            </a>





          </div>



        ))}



      </div>





    </div>


  );


}



export default App;