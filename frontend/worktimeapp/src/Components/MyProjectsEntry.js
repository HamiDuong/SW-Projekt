import React, {Component} from 'react'
import './MyProjectsEntry.css';
import Button from '@mui/material/Button';
import Grid from '@mui/material/Grid';
import { format } from "date-fns";
import ProjectWorkBO from '../API/ProjectWorkBO';
import WorkTimeAppAPI  from '../API/WorkTimeAppAPI';
import BookingBO from '../API/BookingBO';
import BreakBO from '../API/BreakBO';

/**
 * @author [Esra Özkul](https://github.com/EsraOEzkul)
 */

class MyProjectEntry extends Component {
  constructor(props){
    super(props);
    //Hier werden die Änderungen gespeichert.
    this.togglePopups = this.togglePopups.bind(this);
    this.handleClick = this.handleClick.bind(this);
    this.state={
      //Hier werden die States für MyProjectEntry gesetzt.
      start:0,
      startButton: false,
      startActivity: 0,
      endActivity: 0,
      startBreak:0,
      endBreak:0,
      activityId: props.activity.id,
      // activityId: 1,
      typeProjectWork: "projectwork",
      typeBreak: "break",
      startEvent: null,
      endEvent: null,
      eventBookingId: 0,
      timeintervalBookingId: 0,
      // userId: props.user.getID(),
      userId: props.userId,
      workTimeAccountId: 0,
      trigger: false,
    };
}
/**
 * Hier werden die Objekte für Break und Booking erstellt und die entsprechenden API Funktionen werden aufgerufen.
 */
addBreak(){
let newBreakBO = new BreakBO(this.state.startBreak, this.state.endBreak, this.state.startEvent, this.state.endEvent, this.state.typeBreak);
            WorkTimeAppAPI.getAPI().addBreakBooking(newBreakBO)
            let newBookingBO = new BookingBO(this.state.workTimeAccountId, this.state.userId, this.state.typeBreak, this.state.eventBookingId, this.state.timeintervalBookingId)
            WorkTimeAppAPI.getAPI().addBooking(newBookingBO)
            console.log(newBreakBO)
            console.log(newBookingBO)
          
}
/**
 * Hier werden die Objekte für ProjectWork und Booking erstellt und die entsprechenden API Funktionen werden aufgerufen.
 */
addProjectWork(){
  let newProjectWorkBO = new ProjectWorkBO(this.state.startActivity, this.state.endActivity, this.state.startEvent, this.state.endEvent, this.state.typeProjectWork, this.state.activityId);
            WorkTimeAppAPI.getAPI().addProjectWorkBooking(newProjectWorkBO)
            let newBookingBO = new BookingBO(this.state.workTimeAccountId, this.state.userId, this.state.typeProjectWork, this.state.eventBookingId, this.state.timeintervalBookingId)
            WorkTimeAppAPI.getAPI().addBooking(newBookingBO)
            console.log(newProjectWorkBO)
            console.log(newBookingBO)
            console.log('AAAAAA!!!!',this.state.activityId)
}

/**
 * Diese Funktion öffnet den PopUp für die Buttons.
 */
togglePopups() {
  this.setState({
      startButton: true,
  });
}
/**
 * In dieser Funktion läuft der ount für start.
 */
onStart=()=>{
   this.setState({
    start:this.state.start+1,
    
  });
}

/**
 * StartProjectWork starten den Timer.
 * Außerdem wird im state startActivity das aktuelle Datum und Uhrzeit gespeichert.
 * Der Grund dafür ist das der startActivty später für das erstellen von ProjectWorkBO benötigt wird.
 * 
 */

startProjectWork=()=>{
  if(this.state.trigger){
    alert("Please end your break first!");
  }else{
    this.f=setInterval(this.onStart,1000);
  document.getElementById('btn');
  this.setState({
    startActivity: format(new Date(), "yyyy-MM-dd HH:mm:ss")
          },function(){
            console.log('START',this.state.startActivity)
})
  }
}

/**
 * endProjectWork beendet den Timer.
 * Außerdem wird im state endActivity das aktuelle Datum und Uhrzeit gespeichert.
 * Der Grund dafür ist das der endActivty später für das erstellen von ProjectWorkBO benötigt wird.
 */

endProjectWork=()=>{
  clearInterval(this.f);
  document.getElementById('btn');
  this.setState({
    start:0,
    endActivity: format(new Date(), "yyyy-MM-dd HH:mm:ss")
          },
          function(){
              this.addProjectWork()
            } 
            )         
}

/**
 * breakStart startet den Break. Der Timer wird gestoppt.
 * In breakStart wird das aktuelle Datum und Uhrzeit gespeichert.
 * Der Grund dafür ist das der breakStart später für das erstellen von BreakBO benötigt wird.
 */

breakStart=()=>{
    clearInterval(this.f);
    this.setState({
      trigger: true,
      startBreak: format(new Date(), "yyyy-MM-dd HH:mm:ss")
            },function(){
              console.log('START BREAK',this.state.startBreak)
  })

}
/**
 * breakEnd startet den Break. Der Timer wird gestoppt.
 * In breakEnd wird das aktuelle Datum und Uhrzeit gespeichert.
 * Der Grund dafür ist das der breakEnd später für das erstellen von BreakBO benötigt wird.
 */

breakEnd=()=>{
  this.f=setInterval(this.onStart,1000);
  this.setState({
    trigger: false,
    endBreak: format(new Date(), "yyyy-MM-dd HH:mm:ss")
          },function(){
            this.addBreak()
          } 
)
}

/**
 * In dieser Funktion wird der Timer wieder auf Null gestellt.
 */

onReset=()=>{
    clearInterval(this.f);
    document.getElementById('btn');
    this.setState({start:0})
}

/**
 * showing() wird erst angezeigt, sobald der Button für startActivity angeklickt wird.
 */

showing() {
  //Wenn startButton auf True gesetzt ist, wird es angezeigt.
  if (this.state.startButton) {
      console.log('showing läuft')
      return <Grid><Button onClick={this.endProjectWork}>End Activity</Button>
                  <Button onClick={this.breakStart}>Start Break</Button>
                  <Button onClick={this.breakEnd}>End Break</Button>
                  <Button onClick={this.onReset}>Reset</Button>
                  </Grid> 
  } else {
      return <h5>Please start the activity!</h5>
  }
}
/**
 * Mit dieser Funktion wird die Funktion startProjectWork aufgerufen.
 * Außerdem wird startButton auf True gesetzt.
 */

handleClick() {
  this.startProjectWork();
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
                    // startActivity im state wird weitergegeben.
                        value={this.state.startActivity}
                        onClick={this.handleClick}
                        onChange={(newValue) => {
                                    this.startProjektTime(newValue);
                                    }}>
                        Start Activity
                    </Button>
                </Grid>
            {func}
        </div>
    )
}
}
export default MyProjectEntry
