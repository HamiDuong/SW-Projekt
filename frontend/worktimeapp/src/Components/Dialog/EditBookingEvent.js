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
 * @author Ha Mi Duong (https://github.com/HamiDuong)
 * 
 * Dialog für die Bearbeitung von Eventbuchungen
 */
class EditBookingEvent extends Component {
    constructor(props) {
        super(props);
        this.state = {
            booking: this.props.booking,
            time: props.booking.time,
            type: props.booking.type
        };
        this.baseState = this.state;
    }

    // schließen vom Dialog
    handleClose = () => {
        this.props.onClose(null)
    }

    // löschen des Eintrags
    deleteBooking = () => {
        console.log("Booking löschen");
        const { booking } = this.props;
        console.log(booking)

        // Endpunkt entsprechend des Typs wählen

        if (this.state.type == "breakstart") {
            WorkTimeAppAPI.getAPI().deleteBreakStart(this.state.booking).then(booking => {
                console.log("Delete BreakStart");
                console.log(booking);

            });
        }

        if (this.state.type == "breakend") {
            WorkTimeAppAPI.getAPI().deleteBreakEnd(this.state.booking).then(booking => {
                console.log("Delete BreakEnd");
                console.log(booking);
            });
        }

        if (this.state.type == "coming") {
            WorkTimeAppAPI.getAPI().deleteComing(this.state.booking).then(booking => {
                console.log("Delete Coming");
                console.log(booking);
            });
        }

        if (this.state.type == "going") {
            WorkTimeAppAPI.getAPI().deleteGoing(this.state.booking).then(booking => {
                console.log("Delete Going");
                console.log(booking);
            });
        }

        if (this.state.type == "flexdayend") {
            WorkTimeAppAPI.getAPI().deleteFlexDayEnd(this.state.booking).then(booking => {
                console.log("Delete FlexDayEnd");
                console.log(booking);
            });
        }

        if (this.state.type == "flexdaystart") {
            WorkTimeAppAPI.getAPI().deleteFlexDayStart(this.state.booking).then(booking => {
                console.log("Delete FlexDayStart");
                console.log(booking);
            });
        }

        if (this.state.type == "illnessbegin") {
            WorkTimeAppAPI.getAPI().deleteIllnessStart(this.state.booking).then(booking => {
                console.log("Delete IllnessStart");
                console.log(booking);
            });
        }

        if (this.state.type == "illnessend") {
            WorkTimeAppAPI.getAPI().deleteIllnessEnd(this.state.booking).then(booking => {
                console.log("Delete IllnessEnd");
                console.log(booking);
            });
        }

        if (this.state.type == "projectworkstart") {
            WorkTimeAppAPI.getAPI().deleteProjectWorkStart(this.state.booking).then(booking => {
                console.log("Delete ProjectWorkStart");
                console.log(booking);
            });
        }

        if (this.state.type == "projectworkend") {
            WorkTimeAppAPI.getAPI().deleteProjectWorkEnd(this.state.booking).then(booking => {
                console.log("Delete ProjectWorkEnd");
                console.log(booking);
            });
        }

        if (this.state.type == "vacationbegin") {
            WorkTimeAppAPI.getAPI().deleteVacationStart(this.state.booking).then(booking => {
                console.log("Delete VacationStart");
                console.log(booking);

            });
        }

        if (this.state.type == "vacationend") {
            WorkTimeAppAPI.getAPI().deleteVacationEnd(this.state.booking).then(booking => {
                console.log("Delete VacationEnd");
                console.log(booking);
            });
        }
        this.handleClose();

    }

    // Änderungen im State abspeichern
    saveChanges = () => {
        let timehold = document.getElementById("time");
        this.setState({
            time: timehold.value
        }, function () {
            console.log("State für neue Werte");
        });
    }

    // Änderungen abspeichern
    updateBooking = () => {
        let updatedbooking = null;

        let timehold = document.getElementById("time");
        let val = timehold.value

        console.log(this.state.time);

        // Endpunkt entsprechen des Typs wählen
        if (this.state.type == "breakstart") {
            updatedbooking = Object.assign(new BreakStartBO(), this.props.booking);
            updatedbooking.setTime(val);
            WorkTimeAppAPI.getAPI().updateBreakStart(updatedbooking).then(booking => {
                console.log("Update BreakStart");
                console.log(booking);
            });
        }

        if (this.state.type == "breakend") {
            updatedbooking = Object.assign(new BreakEndBO(), this.props.booking);
            updatedbooking.setTime(val);
            WorkTimeAppAPI.getAPI().updateBreakEnd(updatedbooking).then(booking => {
                console.log("Update BreakEnd");
                console.log(booking);
            });
        }

        if (this.state.type == "coming") {
            updatedbooking = Object.assign(new ComingBO(), this.props.booking);
            updatedbooking.setTime(val);
            WorkTimeAppAPI.getAPI().updateComing(updatedbooking).then(booking => {
                console.log("Update Coming");
                console.log(booking);
            });
        }

        if (this.state.type == "going") {
            updatedbooking = Object.assign(new GoingBO(), this.props.booking);
            updatedbooking.setTime(val);
            WorkTimeAppAPI.getAPI().updateGoing(updatedbooking).then(booking => {
                console.log("Update Going");
                console.log(booking);
            });
        }


        if (this.state.type == "flexdayend") {
            updatedbooking = Object.assign(new FlexDayEndBO(), this.props.booking);
            updatedbooking.setTime(val);
            WorkTimeAppAPI.getAPI().updateFlexDayEnd(updatedbooking).then(booking => {
                console.log("Update FlexDayEnd");
                console.log(booking);
            });
        }

        if (this.state.type == "flexdaystart") {
            updatedbooking = Object.assign(new FlexDayStartBO(), this.props.booking);
            updatedbooking.setTime(val);
            WorkTimeAppAPI.getAPI().updateFlexDayStart(updatedbooking).then(booking => {
                console.log("Update FlexDayStart");
                console.log(booking);
            });
        }

        if (this.state.type == "illnessbegin") {
            updatedbooking = Object.assign(new IllnessStartBO(), this.props.booking);
            updatedbooking.setTime(val);
            WorkTimeAppAPI.getAPI().updateIllnessStart(updatedbooking).then(booking => {
                console.log("Update IllnessStart");
                console.log(booking);
                this.props.onClose(booking)
            });
        }

        if (this.state.type == "illnessend") {
            updatedbooking = Object.assign(new IllnessEndBO(), this.props.booking);
            updatedbooking.setTime(val);
            WorkTimeAppAPI.getAPI().updateIllnessEnd(updatedbooking).then(booking => {
                console.log("Update IllnessEnd");
                console.log(booking);
                this.props.onClose(booking)
            });
        }

        if (this.state.type == "projectworkstart") {
            updatedbooking = Object.assign(new ProjectWorkStartBO(), this.props.booking);
            updatedbooking.setTime(val);
            WorkTimeAppAPI.getAPI().updateProjectWorkStart(updatedbooking).then(booking => {
                console.log("Update ProjectWorkStart");
                console.log(booking);
            });
        }

        if (this.state.type == "projectworkend") {
            updatedbooking = Object.assign(new ProjectWorkEndBO(), this.props.booking);
            updatedbooking.setTime(val);
            WorkTimeAppAPI.getAPI().updateProjectWorkEnd(updatedbooking).then(booking => {
                console.log("Update ProjectWorkEnd");
                console.log(booking);
            });
        }

        if (this.state.type == "vacationbegin") {
            updatedbooking = Object.assign(new VacationStartBO(), this.props.booking);
            updatedbooking.setTime(val);
            WorkTimeAppAPI.getAPI().updateVacationStart(updatedbooking).then(booking => {
                console.log("Update VacationStart");
                console.log(booking);
                this.props.onClose(booking)
            });
        }

        if (this.state.type == "vacationend") {
            updatedbooking = Object.assign(new VacationEndBO(), this.props.booking);
            updatedbooking.setTime(val);
            WorkTimeAppAPI.getAPI().updateVacationEnd(updatedbooking).then(booking => {
                console.log("Update VacationEnd");
                console.log(booking);
                this.props.onClose(booking)
            });
        }
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
                        <TextField
                            id="type"
                            label="Type"
                            variant='standard'
                            value={this.state.type}
                            InputLabelProps={{
                                readOnly: true
                            }}
                        >
                        </TextField>
                        <div>
                            <TextField
                                id="time"
                                label="Date"
                                variant="standard"
                                defaultValue={this.state.time}
                                InputLabelProps={{
                                    shrink: true,
                                }}
                            />
                        </div>
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