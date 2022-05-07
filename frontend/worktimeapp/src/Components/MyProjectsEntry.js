import React from 'react'
import './MyProjectsEntry.css';

function MyProjectsEntry({closePopup}) {
  return (
    <div className="popupBackground">
        <div className="popupContainer">
            <div className='titleCloseBtn'>
                <button onClick={() => closePopup(false)}>X</button>
            </div>
            <div className='title'>
                <h1>
                    Aktivität: 
                </h1>
            </div>
            <div className='body'>
             {/* Hier kommt der Timer! */}   

            </div>
            <div className='footer'>
                <button>Start</button>
                <button onClick={() => closePopup(false)} id='cancelBtn'>Beenden</button>
            </div>
        </div>
    </div>
  )
}

export default MyProjectsEntry;