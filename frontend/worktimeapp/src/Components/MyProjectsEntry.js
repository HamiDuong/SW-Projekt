import React from 'react'
import CloseIcon from '@mui/icons-material/Close';

function MyProjectsEntry() {
  return (
    <div className="projectBackground">
        <div className="projectContainer">
            <CloseIcon/>
            <div className='title'>
                <h1>
                    Aktivität: 
                </h1>
            </div>
            <div className='body'></div>
            <div className='footer'>
                <button>Start</button>
                <button>Pause</button>
                <buttin>Ende</buttin>
            </div>
        </div>
    </div>
  )
}

export default MyProjectsEntry;