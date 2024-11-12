import axios from "axios";
import React, {useState} from "react";
import  Axios from "axios";

function App(){
const[directorStats, setDirectorStats] = useState(null);
const[directorName,setDirectorName]= useState("");

const fetchDirectorStats =async (e) =>{
    e.preventDefault();
    try{
        const response= await Axios.get("https://app.codescreen.com/api/assessments/films",{
          params:{directorName},
          headers:{Authorization:'Bearer 8c5996d5-fb89-46c9-8821-7063cfbc18b1'}
    });
    const films=response.data;
    if(films.length > 0 ){
        const bestRatedFilm = films.reduce((max, film) => (film.rating > max.rating?film :max));
        const longestFilmuration =Math.max(...films.map(film => film.length ));
        const averageRating = films.reduce((sum,film) => sum+film.rating, 0) /films.length;
        const shortestDays =Math.min(...films.map(film=> new Date(film.releaseDate).getTime ));

        setDirectorStats({
            setDirectorStats({
                bestRatedFilm: bestRatedFilm.name,
                longestFilmDuration,
                averageRating,
                shortestDays,
              });
            } else {
              setDirectorStats(null); 
            }
          } catch (error) {
            console.error("Error fetching director stats:", error);
            setDirectorStats(null);
          }
        };
      
        return (
          <div className='App'>
            <h1>Films by Director</h1>
            <form onSubmit={fetchDirectorStats} id="input-form">
              <input
                type="text"
                id="input-box"
                placeholder="Enter Director's Name"
                value={directorName}
                onChange={(e) => setDirectorName(e.target.value)}  // Update the directorName on input change
              />
              <button type="submit" id="submit-button">Submit</button>
            </form>
      
            {directorStats ? (
              <div>
                <p id="best-rated-film">Best Rated Film: {directorStats.bestRatedFilm}</p>
                <p id="longest-film">Longest Film Duration: {directorStats.longestFilmDuration} minutes</p>
                <p id="average-rating">Average Rating: {directorStats.averageRating}</p>
                <p id="shortest-days">Shortest Days Between Releases: {directorStats.shortestDays}</p>
              </div>
            ) : (
              <p>No films found for this director.</p>  // Display message if no films found
            )}
          </div>
        );
      }
      
      export default App;

