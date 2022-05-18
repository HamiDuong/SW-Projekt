import React, { Component,useState } from 'react';
import MyProjectsEntry from './MyProjectsEntry';
import './MyProjectTest.css'

//Diese Datei ist ein Platzhalter für den MyProjects

function MyProjectsTest() {

    const [openPopup, setOpenPopup ] =  useState(false)
    
    return(
        <div className="MyProjectsTest">
            <h2>Hier klicken!</h2>
            {/* Das öffnet den Pop-Up mit der onClick Funktion */}
            <button className='openPopup' onClick={() => {
                setOpenPopup(true);
            } }>
                Öffnen
                </button>
            {openPopup && <MyProjectsEntry closePopup={setOpenPopup}/>}
        </div>
    );
}

export default MyProjectsTest;