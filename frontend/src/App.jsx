import "./App.css";
import { useEffect, useState } from "react";
import { getTopJobs } from "./api/jobs";


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




  const filteredJobs = jobs.filter(job => {


    const text =
      (
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




      <div className="controls">


        <input

          type="text"

          placeholder="Search jobs..."

          value={search}

          onChange={
            (e)=>setSearch(e.target.value)
          }

        />



        <select

          value={filter}

          onChange={
            (e)=>setFilter(e.target.value)
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

              Location: {job.location}

            </p>




            <p>

              CV: {job.cv_type}

            </p>





            <span className="score">

              Match Score:
              {" "}
              {job.ai_score}

            </span>





            <br />





            <span className="status">

              Status:
              {" "}
              {job.status}

            </span>





            <br />





            <a

              href={job.url}

              target="_blank"

              rel="noreferrer"

            >

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