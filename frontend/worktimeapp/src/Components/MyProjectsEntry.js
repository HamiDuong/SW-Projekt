import React from 'react'
import './MyProjectsEntry.css';

function MyProjectsEntry({closePopup}) {
    const [time, setTime] = React.useState(0);
    const [timerOn, setTimerOn] = React.useState(false);
    // const [break, setBreak] = React.useState(0);
    // const [breakOn, setBreakOn] = React.useState(false);

    React.useEffect(() => {
        let interval = null;
    
        if (timerOn) {
          interval = setInterval(() => {
            setTime((prevTime) => prevTime + 10);
          }, 10);
        } else if (!timerOn) {
          clearInterval(interval);
        }
        
        // if (breakOn) {
        //   interval = setInterval(() => {
        //     setBreak((prevBreak) => prevBreak + 10);
        //   }, 10);
        // } else if (!breakOn) {
        //   clearInterval(interval);
        // }
       
        return () => clearInterval(interval);
      }, [timerOn]);

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
                <p>
                    Hier kommen die Aktivitäten!
                </p>
            </div>
            <div className='body'>
             {/* Hier kommt der Timer! */}   
                <span>{("0" + Math.floor((time / 60000) % 60)).slice(-2)}:</span>
                <span>{("0" + Math.floor((time / 1000) % 60)).slice(-2)}:</span>
                <span>{("0" + ((time / 10) % 100)).slice(-2)}</span>

            </div>
            <div className='footer'>
                {/* Start Button: */}
                 {!timerOn && time === 0 && ( 
                <button onClick={() => setTimerOn(true)}>Arbeit starten</button>
                )}

                {/* Pause Button:
                  Dazu gehört Start Pause und Ende Pause */}
                {timerOn && 
                  <button onClick={() => setTimerOn(false)}>Start Pause</button>}
                 
                {!timerOn && time > 0 && (
                <button onClick={() => setTimerOn(true)}>Ende Pause</button>
                )}

                
                  
                {/* <button onClick={() => setTimerOn(false)}>Pause einlegen</button>
                 
                
                <button onClick={() => setTimerOn(true)}>Ende Pause</button> */}
                

                {/* Reset Button : */}
                {/* {!timerOn && time > 0 && (
                <button onClick={() => setTime(0)}>Reset</button>
                )} */}
                
                <button onClick={() => setTimerOn(false)}>Ende</button>

                {/* <button onClick={() => closePopup(false)} id='saveBtn'>Speichern</button> */}
                <button onClick={() => closePopup(false)} id='cancelBtn'>Abbrechen</button>
            </div>
        </div>
    </div>
  )
}

export default MyProjectsEntry;