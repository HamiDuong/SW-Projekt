import React from 'react'
import './MyProjectsEntry.css';

function MyProjectsEntry({closePopup}) {
    const [time, setTime] = React.useState(0);
    const [timerOn, setTimerOn] = React.useState(false);

    React.useEffect(() => {
        let interval = null;
    
        if (timerOn) {
          interval = setInterval(() => {
            setTime((prevTime) => prevTime + 10);
          }, 10);
        } else if (!timerOn) {
          clearInterval(interval);
        }
    
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
                {!timerOn && time === 0 && (
                <button onClick={() => setTimerOn(true)}>Start</button>
                )}
                {timerOn && <button onClick={() => setTimerOn(false)}>Ende</button>}
                {!timerOn && time > 0 && (
                <button onClick={() => setTime(0)}>Reset</button>
                )}
                {!timerOn && time > 0 && (
                <button onClick={() => setTimerOn(true)}>Resume</button>
                )}
                <button onClick={() => closePopup(false)} id='cancelBtn'>Beenden</button>
            </div>
        </div>
    </div>
  )
}

export default MyProjectsEntry;