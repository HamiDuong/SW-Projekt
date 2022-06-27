import {
    DialogActions,
    TextField,
    Dialog,
    DialogContent,
    DialogTitle,
    Button,
    Stack
} from '@mui/material';
import React, { Component } from 'react';
import WorkTimeAppAPI from '../../API/WorkTimeAppAPI';

import BreakEndBO from '../../API/EventBOs/BreakEndBO';
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


/**
 * Bearbeitungsfenster für Eventbuchungen
 * 
 * @author [Ha Mi Duong] (https://github.com/HamiDuong)
 */
class EditBookingEvent extends Component {
    constructor(props) {
        super(props);
        this.state = {
            booking: props.booking,
            userId: props.userId,

            time: props.booking.time,
            type: props.booking.type
        };
        this.baseState = this.state;
    }

    handleClose = () => {
        this.props.onClose(null)
    }

    saveChanges = () => {
        let timehold = document.getElementById("time");
        this.setState({
            time: timehold.value
        }, function(){
            console.log("State für neue Werte");
        });
    }
    
    deleteBooking = () => {
        console.log("Booking löschen");
        const { booking } = this.props;

        switch(this.state.type){
            case "breakbegin":
                WorkTimeAppAPI.getAPI().deleteBreakStart(booking.id).then(booking =>{
                    console.log("Delete BreakStart");
                    console.log(booking);
                });
            
            case "breakend":
                WorkTimeAppAPI.getAPI().deleteBreakEnd(booking.id).then(booking =>{
                    console.log("Delete BreakEnd");
                    console.log(booking);
                });

            case "coming":
                WorkTimeAppAPI.getAPI().deleteComing(booking.id).then(booking =>{
                    console.log("Delete Coming");
                    console.log(booking);
                });

            case "going":
                WorkTimeAppAPI.getAPI().deleteGoing(booking.id).then(booking =>{
                    console.log("Delete Going");
                    console.log(booking);
                });

            case "flexdayend":
                WorkTimeAppAPI.getAPI().deleteFlexDayEnd(booking.id).then(booking =>{
                    console.log("Delete FlexDayEnd");
                    console.log(booking);
                });

            case "flexdaystart":
                WorkTimeAppAPI.getAPI().deleteFlexDayStart(booking.id).then(booking =>{
                    console.log("Delete FlexDayStart");
                    console.log(booking);
                });

            case "illnessbegin":
                WorkTimeAppAPI.getAPI().deleteIllnessStart(booking.id).then(booking =>{
                    console.log("Delete IllnessStart");
                    console.log(booking);
                });

            case "illnessend":
                WorkTimeAppAPI.getAPI().deleteIllnessEnd(booking.id).then(booking =>{
                    console.log("Delete IllnessEnd");
                    console.log(booking);
                });

            case "projectworkbegin":
                WorkTimeAppAPI.getAPI().deleteProjectWorkStart(booking.id).then(booking =>{
                    console.log("Delete ProjectWorkStart");
                    console.log(booking);
                });

            case "projectworkend":
                WorkTimeAppAPI.getAPI().deleteProjectWorkEnd(booking.id).then(booking =>{
                    console.log("Delete ProjectWorkEnd");
                    console.log(booking);
                });

            case "vacationbegin":
                WorkTimeAppAPI.getAPI().deleteVacationStart(booking.id).then(booking =>{
                    console.log("Delete VacationStart");
                    console.log(booking);
                });

            case "vacationend":
                WorkTimeAppAPI.getAPI().deleteVacationEnd(booking.id).then(booking =>{
                    console.log("Delete VacationEnd");
                    console.log(booking);
                });                    
        }
        this.handleClose()

    }

    updateBooking = () => {
        let updatedbooking = null;
        switch(this.state.type){
            case "BreakStart":
                updatedbooking = Object.assign(new BreakStartBO(), this.props.booking);
                updatedbooking.setTime(this.state.time);
                WorkTimeAppAPI.getAPI().updateBreakStart(updatedbooking).then(booking =>{
                    console.log("Update BreakStart");
                    console.log(booking);
                });

            case "BreakEnd":
                updatedbooking = Object.assign(new BreakEndBO(), this.props.booking);
                updatedbooking.setTime(this.state.time);
                WorkTimeAppAPI.getAPI().updateBreakEnd(updatedbooking).then(booking =>{
                    console.log("Update BreakEnd");
                    console.log(booking);
                });

            case "Coming":
                updatedbooking = Object.assign(new ComingBO(), this.props.booking);
                updatedbooking.setTime(this.state.time);
                WorkTimeAppAPI.getAPI().updateComing(updatedbooking).then(booking =>{
                    console.log("Update Coming");
                    console.log(booking);
                });

            case "Going":
                updatedbooking = Object.assign(new GoingBO(), this.props.booking);
                updatedbooking.setTime(this.state.time);
                WorkTimeAppAPI.getAPI().updateGoing(updatedbooking).then(booking =>{
                    console.log("Update Going");
                    console.log(booking);
                });

            case "FlexDayEnd":
                updatedbooking = Object.assign(new FlexDayEndBO(), this.props.booking);
                updatedbooking.setTime(this.state.time);
                WorkTimeAppAPI.getAPI().updateFlexDayEnd(updatedbooking).then(booking =>{
                    console.log("Update FlexDayEnd");
                    console.log(booking);
                });

            case "FlexDayStart":
                updatedbooking = Object.assign(new FlexDayStartBO(), this.props.booking);
                updatedbooking.setTime(this.state.time);
                WorkTimeAppAPI.getAPI().updateFlexDayStart(updatedbooking).then(booking =>{
                    console.log("Update FlexDayStart");
                    console.log(booking);
                });

            case "IllnessStart":
                updatedbooking = Object.assign(new IllnessStartBO(), this.props.booking);
                updatedbooking.setTime(this.state.time);
                WorkTimeAppAPI.getAPI().updateIllnessStart(updatedbooking).then(booking =>{
                    console.log("Update IllnessStart");
                    console.log(booking);
                });

            case "IllnessEnd":
                updatedbooking = Object.assign(new IllnessEndBO(), this.props.booking);
                updatedbooking.setTime(this.state.time);
                WorkTimeAppAPI.getAPI().updateIllnessEnd(updatedbooking).then(booking =>{
                    console.log("Update IllnessEnd");
                    console.log(booking);
                });

            case "ProjectWorkStart":
                updatedbooking = Object.assign(new ProjectWorkStartBO(), this.props.booking);
                updatedbooking.setTime(this.state.time);
                WorkTimeAppAPI.getAPI().updateProjectWorkStart(updatedbooking).then(booking =>{
                    console.log("Update ProjectWorkStart");
                    console.log(booking);
                });

            case "ProjectWorkEnd":
                updatedbooking = Object.assign(new ProjectWorkEndBO(), this.props.booking);
                updatedbooking.setTime(this.state.time);
                WorkTimeAppAPI.getAPI().updateProjectWorkEnd(updatedbooking).then(booking =>{
                    console.log("Update ProjectWorkEnd");
                    console.log(booking);
                });

            case "VacationStart":
                updatedbooking = Object.assign(new VacationStartBO(), this.props.booking);
                updatedbooking.setTime(this.state.time);
                WorkTimeAppAPI.getAPI().updateVacationStart(updatedbooking).then(booking =>{
                    console.log("Update VacationStart");
                    console.log(booking);
                });

            case "VacationEnd":
                updatedbooking = Object.assign(new VacationEndBO(), this.props.booking);
                updatedbooking.setTime(this.state.time);
                WorkTimeAppAPI.getAPI().updateVacationEnd(updatedbooking).then(booking =>{
                    console.log("Update VacationEnd");
                    console.log(booking);
                });
        }
        this.handleClose()
    }

    render() { 
        const { classes, show } = this.props
        return (
            show ?
            <Dialog open={show} onClose={this.handleClose} maxWidth='xs'>
                <DialogContent>
                    <DialogTitle>
                        <h2>Edit the Event-Booking</h2>
                    </DialogTitle>
                    <Stack spacing={1}>
                            <TextField
                                id = "type"
                                label = "Type"
                                variant = 'standard'
                                defaultValue={this.state.type}       
                                InputLabelProps={{
                                    readOnly: true
                                }}        
                            >
                            </TextField>                            
                        </Stack>
                            <TextField
                                id = "time"
                                label="Date"
                                variant = "standard"
                                defaultValue={this.state.time}
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
                        onClick={this.updateBooking}
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