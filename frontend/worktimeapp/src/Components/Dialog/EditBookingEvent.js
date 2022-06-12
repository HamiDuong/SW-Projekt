import {
    DialogActions,
    TextField,
    Dialog,
    DialogContent,
    DialogTitle,
    Button
} from '@mui/material';
import React, { Component } from 'react';
import WorkTimeAppAPI from '../../API/WorkTimeAppAPI';

import BreakEndBO from '../API/EventBOs/BreakEndBO';
import BreakStartBO from '../../API/EventBOs/BreakStartBO';
import ComingBO from '../../API/EventBOs/ComingBO';
import GoingBO from '../../API/EventBOs/GoingBO';
import FlexDayEndBO from '../../API/EventBOs/FlexDayEndBO';
import FlexDayStartBO from '../../API/EventBOs/FlexDayStartBO';
import IllnessEndBO from '../../API/EventBOs/IllnessEndBO';
import IllnessStartBO from '../../API/EventBOs/IllnessStartBO';
import ProjectWorkEndBO from '../../API/EventBOs/ProjectWorkEndBO';
import ProjectWorkStartBO from '../../API/EventBOs/ProjectWorkStartBO';
import VacationEndBO from '../../API/EventBOs/VacationEndBO';
import VacationStartBO from '../../API/EventBOs/VacationStartBO';

class EditBookingEvent extends Component {
    constructor(props) {
        super(props);
        this.state = {
            booking: props.booking,
            date: props.booking.time,
            type: props.booking.type
        };
        this.baseState = this.state;
    }

    handleClose = () => {
        this.props.onClose(null)
    }
    
    deleteBooking = (obj) => {
        console.log("Booking löschen")
        // WorkTimeAppAPI.getAPI().deleteBooking(obj)
        switch(this.state.type){
            case "BreakStart":
                WorkTimeAppAPI.getAPI().deleteBreakStart(this.state.booking).then(booking =>{
                    console.log("Delete BreakStart")
                });
            
            case "BreakEnd":
                WorkTimeAppAPI.getAPI().deleteBreakEnd(this.state.booking).then(booking =>{
                    console.log("Delete BreakEnd")
                });

            case "Coming":
                WorkTimeAppAPI.getAPI().deleteComing(this.state.booking).then(booking =>{
                    console.log("Delete Coming")
                });

            case "Going":
                WorkTimeAppAPI.getAPI().deleteGoing(this.state.booking).then(booking =>{
                    console.log("Delete Going")
                });

            case "FlexDayEnd":
                WorkTimeAppAPI.getAPI().deleteFlexDayEnd(this.state.booking).then(booking =>{
                    console.log("Delete FlexDayEnd")
                });

            case "FlexDayBegin":
                WorkTimeAppAPI.getAPI().deleteFlexDayBegin(this.state.booking).then(booking =>{
                    console.log("Delete FlexDayBegin")
                });

            case "IllnessStart":
                WorkTimeAppAPI.getAPI().deleteIllnessStart(this.state.booking).then(booking =>{
                    console.log("Delete IllnessStart")
                });
            case "IllnessEnd":
                WorkTimeAppAPI.getAPI().deleteIllnessEnd(this.state.booking).then(booking =>{
                    console.log("Update Work")
                });
            case "ProjectWorkStart":
                WorkTimeAppAPI.getAPI().deleteProjectWorkStart(this.state.booking).then(booking =>{
                    console.log("Update Work")
                });
            case "ProjectWorkEnd":
                WorkTimeAppAPI.getAPI().deleteProjectWorkEnd(this.state.booking).then(booking =>{
                    console.log("Update Work")
                });
                case "VacationStart":
                    WorkTimeAppAPI.getAPI().deleteVacationStart(this.state.booking).then(booking =>{
                        console.log("Update Work")
                    });
                case "VacationEnd":
                    WorkTimeAppAPI.getAPI().deleteVacationEnd(this.state.booking).then(booking =>{
                        console.log("Update Work")
                    });                    
        }

    }

    saveChanges = () => {
        let datehold = document.getElementById("date");
        this.setState({
            datehold: datehold.value
        }, function(){
            console.log("State für neue Werte");
        });
    }

    updateBooking = () => {
        let updatedbooking = null;
        switch(this.state.type){
            case "Break":
                updatedbooking = Object.assign(new BreakBO(), this.props.booking);
                updatedbooking.setStart(this.state.startdate);
                updatedbooking.setStart(this.state.enddate);
                WorkTimeAppAPI.getAPI().updateBreak(updatedbooking).then(booking =>{
                    console.log("Update Break")
                });
            
            case "Flex Day":
                updatedbooking = Object.assign(new FlexDayBO(), this.props.booking);
                updatedbooking.setStart(this.state.startdate);
                updatedbooking.setStart(this.state.enddate);
                WorkTimeAppAPI.getAPI().updateFlexDay(updatedbooking).then(booking =>{
                    console.log("Update Flex Day")
                });

            case "Illness":
                updatedbooking = Object.assign(new IllnessBO(), this.props.booking);
                updatedbooking.setStart(this.state.startdate);
                updatedbooking.setStart(this.state.enddate);
                WorkTimeAppAPI.getAPI().updateIllness(updatedbooking).then(booking =>{
                    console.log("Update Illness")
                });

            case "Project Duration":
                updatedbooking = Object.assign(new ProjectDurationBO(), this.props.booking);
                updatedbooking.setStart(this.state.startdate);
                updatedbooking.setStart(this.state.enddate);
                WorkTimeAppAPI.getAPI().updateProjectDuration(updatedbooking).then(booking =>{
                    console.log("Update Project Duration")
                });

            case "Projekt Work":
                updatedbooking = Object.assign(new ProjectWorkBO(), this.props.booking);
                updatedbooking.setStart(this.state.startdate);
                updatedbooking.setStart(this.state.enddate);
                WorkTimeAppAPI.getAPI().updateProjectWork(updatedbooking).then(booking =>{
                    console.log("Update Project Work")
                });

            case "Vacation":
                updatedbooking = Object.assign(new VacationBO(), this.props.booking);
                updatedbooking.setStart(this.state.startdate);
                updatedbooking.setStart(this.state.enddate);
                WorkTimeAppAPI.getAPI().updateVacation(updatedbooking).then(booking =>{
                    console.log("Update Vacation")
                });

            case "Work":
                updatedbooking = Object.assign(new WorkBO(), this.props.booking);
                updatedbooking.setStart(this.state.startdate);
                updatedbooking.setStart(this.state.enddate);
                WorkTimeAppAPI.getAPI().updateWork(updatedbooking).then(booking =>{
                    console.log("Update Work")
                });

        }
        //let booking = WorkTimeAppAPI.getAPI().    getBookingByTypeAndId(id, type)
        //gibt das passende Element zurück
        
        //irgendwo müssen neue Werte abgespeichert werden
        //set Attribute auf bestehendes Objekt

        //updateFunktion

    }
    render() { 
        const { classes, show } = this.props
        return (
            show ?
            <Dialog open={show} onClose={this.handleClose} maxWidth='xs'>
                <DialogContent>
                    <DialogTitle>
                        <h2>Edit the booking</h2>
                    </DialogTitle>
                        <TextField
                            id = "startdate"
                            label="Start Date"
                            variant = "standard"
                            format={'YYYY/MM/DD'}
                            type = "date"
                            defaultValue={this.state.booking.start}
                            InputLabelProps={{
                                shrink: true,
                            }}
                        />
                        <TextField
                            id = "enddate"
                            label="End Date"
                            variant = "standard"
                            format={'YYYY/MM/DD'}
                            type = "date"
                            defaultValue={this.state.booking.end}
                            InputLabelProps={{
                                shrink: true,
                            }}
                        />
                </DialogContent>
                <DialogActions>
                    <Button
                        onClick={this.handleClose}
                    >
                        Cancel
                    </Button>
                    <Button
                        onClick={this.deleteBooking}
                    >
                        Delete
                    </Button>
                    <Button
                        onClick={this.saveChanges}
                    >
                        Edit
                    </Button>
                </DialogActions>
            </Dialog>
            : null
        );
    }
}
 
export default EditBookingEvent;