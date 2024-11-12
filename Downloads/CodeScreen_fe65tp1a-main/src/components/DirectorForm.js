import React, {useState} from "react";

function DirectorForm({onSubmit})  {
    const [directorName, setDirectorName] = useState('')

    const handleChange =(event) => {
        setDirectorName(event.target.value);
    };
    const handleSubmit =(event)=> {
        event.preventDefault();
        onSubmit(directorName);
        setDirectorName('');
    };
    return (
        <form id ="input-form" onSubmit={handleSubmit}>
          <label htmlFor="input-box">Enter Director's Name:</label>  
          <input
          id="input-box"
          type="text"
          value={directorName}
          onChange={(e) => setDirectorName(e.target.value)}
          />
        <button type ="submit">Submit</button> 
        </form>


    )
    
}
export default DirectorForm;