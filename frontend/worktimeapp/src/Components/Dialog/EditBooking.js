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

import BreakBO from '../../API/BreakBO';
import FlexDayBO from '../../API/FlexDayBO';
import IllnessBO from '../../API/IllnessBO';
import ProjectDurationBO from '../../API/ProjectDurationBO';
import ProjectWorkBO from '../../API/ProjectWorkBO';
import VacationBO from '../../API/VacationBO';
import WorkBO from '../../API/WorkBO';

class EditBooking extends Component {
    constructor(props) {
        super(props);
        this.state = {
            booking: props.booking,

            startdate: props.booking.start,
            enddate:props.booking.end,
            type: props.booking.type
        };
        this.baseState = this.state;
    }

    handleClose = () => {
        this.props.onClose(null)
    }
    
    deleteBooking = (obj) => {
        console.log("Booking löschen")

        const { booking } = this.props;

        switch(this.state.type){
            case "Break":
                WorkTimeAppAPI.getAPI().deleteBreak(booking.getId()).then(booking =>{
                    console.log("Delete Break");
                    console.log(booking);
                });
            
            case "Flex Day":
                WorkTimeAppAPI.getAPI().deleteFlexDay(booking.getId()).then(booking =>{
                    console.log("Delete Flex Day");
                    console.log(booking);
                });

            case "Illness":
                WorkTimeAppAPI.getAPI().deleteIllness(booking.getId()).then(booking =>{
                    console.log("Delete Illness");
                    console.log(booking);
                });

            case "Project Duration":
                WorkTimeAppAPI.getAPI().deleteProjectDuration(booking.getId()).then(booking =>{
                    console.log("Delete Project Duration");
                    console.log(booking);
                });

            case "Projekt Work":
                WorkTimeAppAPI.getAPI().deleteProjectWork(booking.getId()).then(booking =>{
                    console.log("Delete Project Work");
                    console.log(booking);
                });

            case "Vacation":
                WorkTimeAppAPI.getAPI().deleteVacation(booking.getId()).then(booking =>{
                    console.log("Delete Vacation");
                    console.log(booking);
                });

            case "Work":
                WorkTimeAppAPI.getAPI().deleteWork(booking.getId()).then(booking =>{
                    console.log("Delete Work");
                    console.log(booking);
                });
        }

    }

    // saveChanges = () => {
    //     let starthold = document.getElementById("startdate");
    //     let endhold = document.getElementById("enddate");
    //     this.setState({
    //         startdate: starthold.value,
    //         enddate: endhold.value,
    //     }, function(){
    //         console.log("State für neue Werte");
    //     });
    // }

    updateBooking = () => {
        let starthold = document.getElementById("startdate");
        let endhold = document.getElementById("enddate");
        this.setState({
            startdate: starthold.value,
            enddate: endhold.value,
        }, function(){
            console.log("State für neue Werte");
        });

        let updatedbooking = null;
        switch(this.state.type){
            case "Break":
                updatedbooking = Object.assign(new BreakBO(), this.props.booking);
                updatedbooking.setStart(this.state.startdate);
                updatedbooking.setStart(this.state.enddate);
                WorkTimeAppAPI.getAPI().updateBreak(updatedbooking).then(booking =>{
                    console.log("Update Break");
                    console.log(booking);
                });
            
            case "Flex Day":
                updatedbooking = Object.assign(new FlexDayBO(), this.props.booking);
                updatedbooking.setStart(this.state.startdate);
                updatedbooking.setStart(this.state.enddate);
                WorkTimeAppAPI.getAPI().updateFlexDay(updatedbooking).then(booking =>{
                    console.log("Update Flex Day");
                    console.log(booking);
                });

            case "Illness":
                updatedbooking = Object.assign(new IllnessBO(), this.props.booking);
                updatedbooking.setStart(this.state.startdate);
                updatedbooking.setStart(this.state.enddate);
                WorkTimeAppAPI.getAPI().updateIllness(updatedbooking).then(booking =>{
                    console.log("Update Illness");
                    console.log(booking);
                });

            case "Project Duration":
                updatedbooking = Object.assign(new ProjectDurationBO(), this.props.booking);
                updatedbooking.setStart(this.state.startdate);
                updatedbooking.setStart(this.state.enddate);
                WorkTimeAppAPI.getAPI().updateProjectDuration(updatedbooking).then(booking =>{
                    console.log("Update Project Duration");
                    console.log(booking);
                });

            case "Projekt Work":
                updatedbooking = Object.assign(new ProjectWorkBO(), this.props.booking);
                updatedbooking.setStart(this.state.startdate);
                updatedbooking.setStart(this.state.enddate);
                WorkTimeAppAPI.getAPI().updateProjectWork(updatedbooking).then(booking =>{
                    console.log("Update Project Work");
                    console.log(booking);
                });

            case "Vacation":
                updatedbooking = Object.assign(new VacationBO(), this.props.booking);
                updatedbooking.setStart(this.state.startdate);
                updatedbooking.setStart(this.state.enddate);
                WorkTimeAppAPI.getAPI().updateVacation(updatedbooking).then(booking =>{
                    console.log("Update Vacation");
                    console.log(booking);
                });

            case "Work":
                updatedbooking = Object.assign(new WorkBO(), this.props.booking);
                updatedbooking.setStart(this.state.startdate);
                updatedbooking.setStart(this.state.enddate);
                WorkTimeAppAPI.getAPI().updateWork(updatedbooking).then(booking =>{
                    console.log("Update Work");
                    console.log(booking);
                });

        }
        this.handleClose();
    }

    render() { 
        const { classes, show } = this.props
        return (
            show ?
            <Dialog open={show} onClose={this.handleClose} maxWidth='xs'>
                <DialogContent>
                    <DialogTitle>
                        <h2>Edit the Interval-Booking</h2>
                    </DialogTitle>
                        <TextField
                            id = "startdate"
                            label="Start Date"
                            variant = "standard"
                            defaultValue={this.state.booking.start}
                            InputLabelProps={{
                                shrink: true,
                            }}
                        />
                        <TextField
                            id = "enddate"
                            label="End Date"
                            variant = "standard"
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
 
export default EditBooking;