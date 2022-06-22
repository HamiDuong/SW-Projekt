import React, {Component} from 'react'
import './MyProjectsEntry.css';
import Button from '@mui/material/Button';
import Grid from '@mui/material/Grid';


/**
 * @author [Esra Özkul](https://github.com/EsraOEzkul)
 */

// function MyProjectsEntry({closePopup}) {
    
//   //Hier werden die Konstanten gesetzt, setTime fängt immer mit Null an. 
//   //Es wird false eingesetzt, da false ein default Value ist
//     const [time, setTime] = React.useState(0);
//     const [timerOn, setTimerOn] = React.useState(false);
//     const [startTimeProjectWork, setStartTimeProjectWork] = React.useState(0);
    

//     React.useEffect(() => {
//         //Der Grund für Null ist, da es der geleiche Hook ist
//         let interval = null;
//         //setInterval ist JavaSkript Methode (Arrow Funktion)
//         if (timerOn) {
//           interval = setInterval(() => {
//             // Hier wird initalisiert in 10 Millisekunden, 
//             // Zunahme von Zeit wird hier bestimmt
//             setTime((prevTime) => prevTime + 10);
//           }, 10);
//         } else if (!timerOn) {
//           clearInterval(interval);
//         }
       
//         return () => clearInterval(interval);
//       }, [timerOn]);

//     function startButton(timer){
//       let datetime = new Date();
//       let startTime = datetime.today()
//         setTimerOn(timer);
//         setStartTimeProjectWork(startTime);
//         console.log(startTimeProjectWork);
//         console.log(startTime);
        
//     } 
//   return (

//     <div className="popupBackground">
//         <div className="popupContainer">
//             <div className='titleCloseBtn'>
//                 <button onClick={() => closePopup(false)}>X</button>
//             </div>
//             <div className='title'>
//             </div>
//             <div className='body'>
//              {/* Hier kommt der Timer! */}   
//              {/** Minuten */}
//                 <span>{("0" + Math.floor((time / 60000) % 60)).slice(-2)}:</span>
//               {/** Sekunden */}
//                 <span>{("0" + Math.floor((time / 1000) % 60)).slice(-2)}:</span>
//               {/** Millisekunden */}
//                 <span>{("0" + ((time / 10) % 100)).slice(-2)}</span>

//             </div>
//             <div className='footer'>
//                 {/* Start Button: */}
//                  {!timerOn && time === 0 && ( 
//                 <button onClick={() => setTimerOn(true)}>Start activity</button>
//                 )}
                

//                 {/* Ende Button */}
//                 {timerOn > 0 &&
//                 <button onClick={() => closePopup(false)}>end Activity</button>
//                 }
                
//                 {/* Pause Button:
//                   Dazu gehört Start Pause und Ende Pause */}
//                 {timerOn && 
//                   <button onClick={() => startButton(true)}>Start break</button>}
                 
//                 {!timerOn && time > 0 && (
//                 <button onClick={() => setTimerOn(true)}>End break</button>
//                 )}

//                 {/* <button onClick={() => closePopup(false)} id='saveBtn'>Speichern</button> */}
//                 <button onClick={() => closePopup(false)} id='cancelBtn'>Cancel</button>
//                 {/* <button onClick={this.closePopup} id='cancelBtn'>close me</button> */}
//             </div>
//         </div>
//     </div>
//   )
// }

// export default MyProjectsEntry;

// class MyProjectsEntry extends Component {
//   constructor(props) {
//     super(props);
//     this.state = {
//       time : 0,
//       timeOn : false,
//       setTime: 0,
//       startTimeProjectWork: 0,
//       endTimeProjectWork: 0,
//       startTimeBreak: 0,
//       endTimeBreak: 0,
//       closePopupActivity: false,
//   }}

//   useEffect = () => {
//       //Der Grund für Null ist, da es der geleiche Hook ist
//       let interval = null;
//       //setInterval ist JavaSkript Methode (Arrow Funktion)
//           if (this.timerOn) {
//           interval = setInterval(() => {
//           // Hier wird initalisiert in 10 Millisekunden, 
//           // Zunahme von Zeit wird hier bestimmt
//           this.setTime((prevTime) => prevTime + 10);
//           }, 10);
//           } else if (!this.timerOn) {
//           clearInterval(interval);
//           }
           
//             return () => clearInterval(interval);
//         }

//   startButton = (timer) => {
//     let datetime = new Date();
//     let startTime = datetime.today();
//         this.setState({
//             setTimerOn: timer,
//             setStartTimeProjectWork: startTime,
//             },
//                 console.log(this.startTimeProjectWork),
//                 console.log(this.startTime))
                    
//                 }

//   closePopup (){
//     this.setState({
//         closePopupActivity: true
//     });
//   }
  
  
  
//   render() { 
//     return ( 
//       <div className="popupBackground">
//         <div className="popupContainer">
//                  <div className='titleCloseBtn'>
//                       <button onClick={() => this.closePopup()}>X</button>
//                  </div>
//                 <div className='title'>
//                    </div>
//                    <div className='body'>
//                     {/* Hier kommt der Timer! */}   
//                     {/** Minuten */}
//                        <span>{("0" + Math.floor((this.time / 60000) % 60)).slice(-2)}:</span>
//                      {/** Sekunden */}
//                        <span>{("0" + Math.floor((this.time / 1000) % 60)).slice(-2)}:</span>
//                      {/** Millisekunden */}
//                        <span>{("0" + ((this.time / 10) % 100)).slice(-2)}</span>
      
//                    </div>
//                    <div className='footer'>
//                        {/* Start Button: */}
//                         {!this.timerOn && this.time === 0 && ( 
//                        <button onClick={() => this.setTimerOn(true)}>Start activity</button>
//                        )}
                      
      
//                        {/* Ende Button */}
//                       {this.timerOn > 0 &&
//                        <button onClick={() => this.closePopup(false)}>end Activity</button>
//                        }
                      
//                       {/* Pause Button:
//                          Dazu gehört Start Pause und Ende Pause */}
//                        {this.timerOn && 
//                          <button onClick={() => this.startButton(true)}>Start break</button>}
                       
//                        {!this.timerOn && this.time > 0 && (
//                        <button onClick={() => this.setTimerOn(true)}>End break</button>
//                        )}
      
//                        {/* <button onClick={() => closePopup(false)} id='saveBtn'>Speichern</button> */}
//                        <button onClick={() => this.closePopup(false)} id='cancelBtn'>Cancel</button>
//                        {/* <button onClick={this.closePopup} id='cancelBtn'>close me</button> */}
//                    </div>
//                </div>
//            </div>

//      );
//   }
// }
 
// export default MyProjectsEntry;


class MyProjectEntry extends Component {
  constructor(props){
    super(props);
    this.togglePopups = this.togglePopups.bind(this);
    this.handleClick = this.handleClick.bind(this);
    this.state={
      start:0,
      startButton: false,
    };
}

togglePopups() {
  this.setState({
      startButton: true,
  });
}
onStart=()=>{
   this.setState({start:this.state.start+1});
}
timer=()=>{
  this.f=setInterval(this.onStart,1000);
  document.getElementById('btn');
}
onPause=()=>{
    clearInterval(this.f);
}
onReset=()=>{
    clearInterval(this.f);
    document.getElementById('btn');
    this.setState({start:0})
}
showing() {
  if (this.state.startButton) {
      console.log('showing läuft')
      return <div><Button onClick={this.onPause}>End Activity</Button>
                  <Button onClick={this.onReset}>Reset</Button></div>
      
  } else {
      return <h3>You didn't start the project</h3>
  }
}

handleClick() {
  //Hier kommt die AddProjectWorkBO
  // this.addTimeIntervalBooking();
  this.timer();
  this.setState({
      startButton: true,
  });
  console.log('Hallooohhooo')
}

render(){
  const func = this.showing()
    return(
        <div>
          <h1>{this.state.start}</h1>
            <Grid xs={12} item>
                    <Button
                        onClick={this.handleClick}>
                        Start Activity
                    </Button>
                </Grid>
            {/* <Button onClick={this.onPause}>Stop</Button>
            <Button onClick={this.onReset}>Reset</Button> */}
            {func}

        </div>
    )
}
}
export default MyProjectEntry
