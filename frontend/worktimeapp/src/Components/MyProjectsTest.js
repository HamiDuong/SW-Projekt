import React, { Component,useState } from 'react';
import MyProjectsEntry from './MyProjectsEntry';


function MyProjectsTest() {

    const [openPopup, setOpenPopup ] =  useState(false)
    return(
        <div className="MyProjectsTest">
            <h2>Hier klicken!</h2>
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