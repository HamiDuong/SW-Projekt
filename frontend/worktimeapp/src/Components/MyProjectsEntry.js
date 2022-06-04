import React from 'react'
import './MyProjectsEntry.css';

/**
 * @author [Esra Özkul](https://github.com/EsraOEzkul)
 */

function MyProjectsEntry({closePopup}) {
    
  //Hier werden die Konstanten gesetzt, setTime fängt immer mit Null an. 
  //Es wird false eingesetzt, da false ein default Value ist
    const [time, setTime] = React.useState(0);
    const [timerOn, setTimerOn] = React.useState(false);

    React.useEffect(() => {
        //Der Grund für Null ist, da es der geleiche Hook ist
        let interval = null;
        //setInterval ist JavaSkript Methode (Arrow Funktion)
        if (timerOn) {
          interval = setInterval(() => {
            // Hier wird initalisiert in 10 Millisekunden, 
            // Zunahme von Zeit wird hier bestimmt
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
             {/** Minuten */}
                <span>{("0" + Math.floor((time / 60000) % 60)).slice(-2)}:</span>
              {/** Sekunden */}
                <span>{("0" + Math.floor((time / 1000) % 60)).slice(-2)}:</span>
              {/** Millisekunden */}
                <span>{("0" + ((time / 10) % 100)).slice(-2)}</span>

            </div>
            <div className='footer'>
                {/* Start Button: */}
                 {!timerOn && time === 0 && ( 
                <button onClick={() => setTimerOn(true)}>Arbeit starten</button>
                )}
                

                {/* Ende Button */}
                {timerOn > 0 &&
                <button onClick={() => closePopup(false)}>Arbeit beenden</button>
                }
                
                {/* Pause Button:
                  Dazu gehört Start Pause und Ende Pause */}
                {timerOn && 
                  <button onClick={() => setTimerOn(false)}>Pause starten</button>}
                 
                {!timerOn && time > 0 && (
                <button onClick={() => setTimerOn(true)}>Pause beenden</button>
                )}

                {/* <button onClick={() => closePopup(false)} id='saveBtn'>Speichern</button> */}
                <button onClick={() => closePopup(false)} id='cancelBtn'>Abbrechen</button>
            </div>
        </div>
    </div>
  )
}

export default MyProjectsEntry;