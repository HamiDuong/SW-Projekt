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

/**
 * @author Ha Mi Duong (https://github.com/HamiDuong)
 * 
 * Dialog für die Bearbeitung von Intervalbuchungen
 */
class EditBooking extends Component {
    constructor(props) {
        super(props);

        let startdates = '', enddates = '', types = "";

        if (props.booking) {
            startdates = props.booking.start;
            enddates = props.booking.end;
            types = props.booking.type;
        }
        this.state = {
            booking: this.props.booking,

            startdate: startdates,
            enddate: enddates,
            type: types
        };
        this.baseState = this.state;
    }

    // Schließen vom Dialog
    handleClose = () => {
        this.props.onClose(null);
    }

    printState = () => {
        console.log("Booking", this.state.booking);
        console.log(this.state.startdate);
        console.log(this.state.enddate);
        console.log(this.state.type);
    }
    
    // Löschen der Buchung
    deleteBooking = (obj) => {
        console.log("Booking löschen");

        const { booking } = this.props;
        console.log(this.state.type);
        console.log(booking);
        if ((this.state.type) === "ProjectWork") {
            let ProjectWorkBOs = ProjectWorkBO.fromJSON(booking)
            WorkTimeAppAPI.getAPI().deleteProjectWork(ProjectWorkBOs[0].getID()).then(booking => {
                console.log("Delete Project Work");
                console.log(booking);
            });
        }
        else if ((this.state.type) === "Vacation") {
            let VacationBOs = VacationBO.fromJSON(booking)
            WorkTimeAppAPI.getAPI().deleteVacation(VacationBOs[0].getID()).then(booking => {
                console.log("Delete Vacation");
                console.log(booking);
            });
        }
        else if ((this.state.type) === "Break") {
            let BreakBOs = BreakBO.fromJSON(booking)
            WorkTimeAppAPI.getAPI().deleteBreak(BreakBOs[0].getID()).then(booking => {
                console.log("Delete Break");
                console.log(booking);
            });
        }
        else if ((this.state.type) === "FlexDay") {
            let FlexDayBOs = FlexDayBO.fromJSON(booking)
            WorkTimeAppAPI.getAPI().deleteFlexDay(FlexDayBOs[0].getID()).then(booking => {
                console.log("Delete Flex Day");
                console.log(booking);
            });
        }
        else if ((this.state.type) === "Illness") {
            let IllnessBOs = BreakBO.fromJSON(booking)
            WorkTimeAppAPI.getAPI().deleteIllness(IllnessBOs[0].getID()).then(booking => {
                console.log("Delete Illness");
                console.log(booking);
            });
        }
        else if ((this.state.type) === "ProjectDuration") {
            let ProjectDurationBOs = ProjectDurationBO.fromJSON(booking)
            WorkTimeAppAPI.getAPI().deleteProjectDuration(ProjectDurationBOs[0].getID()).then(booking => {
                console.log("Delete Project Duration");
                console.log(booking);
            });
        }
        else if ((this.state.type) === "Work") {
            let WorkBOs = WorkBO.fromJSON(booking)
            WorkTimeAppAPI.getAPI().deleteWork(WorkBOs[0].getID()).then(booking => {
                console.log("Delete Project Duration");
                console.log(booking);
            });
        }
        this.handleClose();

    }

    // neue Werte der Buchung im State speichern
    saveChanges = () => {
        let starthold = document.getElementById("startdate");
        let endhold = document.getElementById("enddate");
        this.setState({
            startdate: starthold.value,
            enddate: endhold.value,
        }, function () {
            console.log("State für neue Werte");
            console.log(this.state.startdate);
        });
    }

    componentDidMount() {
        console.log("EditBooking ist gemountet");
        console.log(this.state.booking);

    }

    // Änderung der Intervalbuchung abspeichern
    updateBooking = () => {
        let starthold = document.getElementById("startdate");
        let endhold = document.getElementById("enddate");
        this.setState({
            startdate: starthold.value,
            enddate: endhold.value,
        }, function () {
            console.log("State für neue Werte");
        });

        let updatedbooking = null;

        if (this.state.type == "Break") {
            updatedbooking = Object.assign(new BreakBO(), this.props.booking);
            updatedbooking.setStart(this.state.startdate);
            // updatedbooking.setEnd(this.state.enddate);
            WorkTimeAppAPI.getAPI().updateBreak(updatedbooking).then(booking => {
                console.log("Update Break");
                console.log(booking);
                this.props.onClose(booking);

            });
        }

        if (this.state.type == "FlexDay") {
            updatedbooking = Object.assign(new FlexDayBO(), this.props.booking);
            updatedbooking.setStart(this.state.startdate);
            updatedbooking.setEnd(this.state.enddate);
            WorkTimeAppAPI.getAPI().updateFlexDay(updatedbooking).then(booking => {
                console.log("Update Flex Day");
                console.log(booking);
                this.props.onClose(booking)
            });
        }

        if (this.state.type == "Illness") {
            updatedbooking = Object.assign(new IllnessBO(), this.props.booking);
            updatedbooking.setStart(this.state.startdate);
            updatedbooking.setEnd(this.state.enddate);
            WorkTimeAppAPI.getAPI().updateIllness(updatedbooking).then(booking => {
                console.log("Update Illness");
                console.log(booking);
                this.props.onClose(booking);
            });
        }

        if (this.state.type == "ProjectDuration") {
            updatedbooking = Object.assign(new ProjectDurationBO(), this.props.booking);
            updatedbooking.setStart(this.state.startdate);
            updatedbooking.setEnd(this.state.enddate);
            console.log("API CALL", updatedbooking);
            WorkTimeAppAPI.getAPI().updateProjectDuration(updatedbooking).then(booking => {
                console.log("Update Project Duration");
                console.log(booking);
                this.props.onClose(booking);
            });
        }

        if (this.state.type == "ProjectWork") {
            updatedbooking = Object.assign(new ProjectWorkBO(), this.props.booking);
            updatedbooking.setStart(this.state.startdate);
            updatedbooking.setEnd(this.state.enddate);
            WorkTimeAppAPI.getAPI().updateProjectWork(updatedbooking).then(booking => {
                console.log("Update Project Work");
                console.log(booking);
                this.props.onClose(booking);
            });
        }

        if (this.state.type == "Vacation") {
            updatedbooking = Object.assign(new VacationBO(), this.props.booking);
            updatedbooking.setStart(this.state.startdate);
            updatedbooking.setEnd(this.state.enddate);
            WorkTimeAppAPI.getAPI().updateVacation(updatedbooking).then(booking => {
                console.log("Update Vacation");
                console.log(booking);
                this.props.onClose(booking);
            });
        }

        if (this.state.type == "Work") {
            updatedbooking = Object.assign(new WorkBO(), this.props.booking);
            updatedbooking.setStart(this.state.startdate);
            updatedbooking.setEnd(this.state.enddate);
            WorkTimeAppAPI.getAPI().updateWork(updatedbooking).then(booking => {
                console.log("Update Work");
                console.log(booking);
                this.props.onClose(booking);
            });
        }

        //this.handleClose();
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
                            id="type"
                            label="Type"
                            variant='standard'
                            defaultValue={this.state.booking.type}
                            onChange={this.saveChanges}
                            InputLabelProps={{
                                readOnly: true
                            }}
                        >
                        </TextField>
                        <div>
                            <TextField
                                id="startdate"
                                label="Start Date"
                                variant="standard"
                                defaultValue={this.state.booking.start}
                                onChange={this.saveChanges}
                                InputLabelProps={{
                                    shrink: true,
                                }}
                            />
                            <TextField
                                id="enddate"
                                label="End Date"
                                variant="standard"
                                onChange={this.saveChanges}
                                defaultValue={this.state.booking.end}
                                InputLabelProps={{
                                    shrink: true,
                                }}
                            />
                        </div>
                    </DialogContent>
                    <DialogActions>
                        <Button
                            onClick={this.printState}
                        >
                            State printen
                        </Button>
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
