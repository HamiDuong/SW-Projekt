// import {
//     DialogActions,
//     TextField,
//     Dialog,
//     DialogContent,
//     DialogTitle,
//     Button
// } from '@mui/material';
// import React, { Component } from 'react';
// import WorkTimeAppAPI from '../../API/WorkTimeAppAPI';

// import BreakBO from '../../API/BreakBO';
// import FlexDayBO from '../../API/FlexDayBO';
// import IllnessBO from '../../API/IllnessBO';
// import ProjectDurationBO from '../../API/ProjectDurationBO';
// import ProjectWorkBO from '../../API/ProjectWorkBO';
// import VacationBO from '../../API/VacationBO';
// import WorkBO from '../../API/WorkBO';

// class EditBooking extends Component {
//     constructor(props) {
//         super(props);
//         this.state = {
//             booking: props.booking,

//             startdate: props.booking.start,
//             enddate:props.booking.end,
//             type: props.booking.type
//         };
//         this.baseState = this.state;
//     }

//     handleClose = () => {
//         this.props.onClose(null)
//     }
    
//     deleteBooking = (obj) => {
//         console.log("Booking löschen")
//         // WorkTimeAppAPI.getAPI().deleteBooking(obj)

//     }

//     saveChanges = () => {
//         let starthold = document.getElementById("startdate");
//         let endhold = document.getElementById("enddate");
//         this.setState({
//             startdate: starthold.value,
//             enddate: endhold.value,
//         }, function(){
//             console.log("State für neue Werte");
//         });
//     }

//     updateBooking = () => {
//         let updatedbooking = null;
//         switch(this.state.type){
//             case "Break":
//                 updatedbooking = Object.assign(new BreakBO(), this.props.booking);
//                 updatedbooking.setStart(this.state.startdate);
//                 updatedbooking.setStart(this.state.enddate);
//                 // WorkTimeAppAPI.getAPI().updateBreak(updatedbooking).then(booking =>{
//                 //     console.log("Update Break")
//                 // });
            
//             case "Flex Day":
//                 updatedbooking = Object.assign(new FlexDayBO(), this.props.booking);
//                 updatedbooking.setStart(this.state.startdate);
//                 updatedbooking.setStart(this.state.enddate);
//                 // WorkTimeAppAPI.getAPI().updateFlexDay(updatedbooking).then(booking =>{
//                 //     console.log("Update Flex Day")
//                 // });

//             case "Illness":
//                 updatedbooking = Object.assign(new IllnessBO(), this.props.booking);
//                 updatedbooking.setStart(this.state.startdate);
//                 updatedbooking.setStart(this.state.enddate);
//                 // WorkTimeAppAPI.getAPI().updateIllness(updatedbooking).then(booking =>{
//                 //     console.log("Update Illness")
//                 // });

//             case "Project Duration":
//                 updatedbooking = Object.assign(new ProjectDurationBO(), this.props.booking);
//                 updatedbooking.setStart(this.state.startdate);
//                 updatedbooking.setStart(this.state.enddate);
//                 // WorkTimeAppAPI.getAPI().updateBreak(updatedbooking).then(booking =>{
//                 //     console.log("Update Break")
//                 // });

            // case "Projekt Work":
            //     updatedbooking = Object.assign(new ProjectWorkBO(), this.props.booking);
            //     updatedbooking.setStart(this.state.startdate);
            //     updatedbooking.setStart(this.state.enddate);
            //     //newBooking = WorkTimeAppAPI.getAPI().updateProjectWork(obj)

            // case "Vacation":
            //     updatedbooking = Object.assign(new VacationBO(), this.props.booking);
            //     updatedbooking.setStart(this.state.startdate);
            //     updatedbooking.setStart(this.state.enddate);
            //     //newBooking = WorkTimeAppAPI.getAPI().updateVacation(obj)

            // case "Work":
            //     updatedbooking = Object.assign(new WorkBO(), this.props.booking);
            //     updatedbooking.setStart(this.state.startdate);
                // updatedbooking.setStart(this.state.enddate);
                //newBooking = WorkTimeAppAPI.getAPI().updateWork(obj)

//         }
//         //let booking = WorkTimeAppAPI.getAPI().    getBookingByTypeAndId(id, type)
//         //gibt das passende Element zurück
        
//         //irgendwo müssen neue Werte abgespeichert werden
//         //set Attribute auf bestehendes Objekt

//         //updateFunktion

//     }
//     render() { 
//         const { classes, show } = this.props
//         return (
//             show ?
//             <Dialog open={show} onClose={this.handleClose} maxWidth='xs'>
//                 <DialogContent>
//                     <DialogTitle>
//                         <h2>Edit the booking</h2>
//                     </DialogTitle>
//                         <TextField
//                             id = "startdate"
//                             label="Start Date"
//                             variant = "standard"
//                             format={'YYYY/MM/DD'}
//                             type = "date"
//                             defaultValue={this.state.booking.start}
//                             InputLabelProps={{
//                                 shrink: true,
//                             }}
//                         />
//                         <TextField
//                             id = "enddate"
//                             label="End Date"
//                             variant = "standard"
//                             format={'YYYY/MM/DD'}
//                             type = "date"
//                             defaultValue={this.state.booking.end}
//                             InputLabelProps={{
//                                 shrink: true,
//                             }}
//                         />
//                 </DialogContent>
//                 <DialogActions>
//                     <Button
//                         onClick={this.handleClose}
//                     >
//                         Cancel
//                     </Button>
//                     <Button
//                         onClick={this.deleteBooking}
//                     >
//                         Delete
//                     </Button>
//                     <Button
//                         onClick={this.saveChanges}
//                     >
//                         Edit
//                     </Button>
//                 </DialogActions>
//             </Dialog>
//             : null
//         );
//     }
// }
 
// export default EditBooking;