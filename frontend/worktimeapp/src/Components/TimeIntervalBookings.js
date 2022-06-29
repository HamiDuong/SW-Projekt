import React, { Component } from 'react';
import InputLabel from '@mui/material/InputLabel';
import MenuItem from '@mui/material/MenuItem';
import FormControl from '@mui/material/FormControl';
import Select from '@mui/material/Select';
import TextField from '@mui/material/TextField';
import Button from '@mui/material/Button';
import Grid from '@mui/material/Grid';
import Card from '@mui/material/Card';
import Typography from '@mui/material/Typography';
import AccessTimeIcon from '@mui/icons-material/AccessTime';
import { AdapterDateFns } from '@mui/x-date-pickers/AdapterDateFns';
import { LocalizationProvider } from '@mui/x-date-pickers/LocalizationProvider';
import { DateTimePicker } from '@mui/x-date-pickers/DateTimePicker';
import SelectEventDialog from './SelectEventDialog';
import SelectEndEventDialog from './SelectEndEventDialog';
import VacationBO from '../API/VacationBO';
import IllnessBO from '../API/IllnessBO'
import WorkBO from '../API/WorkBO'
import BookingBO from '../API/BookingBO';
import BreakBO from '../API/BreakBO';
import FlexDayBO from '../API/FlexDayBO';
import ProjectWorkBO from '../API/ProjectWorkBO';
import WorkTimeAppAPI from '../API/WorkTimeAppAPI';
import { format } from "date-fns";


{/* 
@author Mihriban Dogan (https://github.com/mihriban-dogan)
TimeIntervalBooking stellt die Form für Zeitintervall Buchungen dar
*/}


class TimeIntervalBookings extends Component {
    constructor(props) {
        super(props);

        this.state = {
            start: Date,
            end: Date,
            type: "",
            project: null,
            startEvent: null,
            endEvent: null,
            workTimeAccountId: 0,
            userId: 1,
            showSelectEventDialog: false,
            showSelectEndEventDialog: false,
            eventBookingId: 0,
            timeintervalBookingId: 0,
            activityId: null,
            vacationIllnessEvents: [],
            projects: [],
            activities: [],
            event: Date

        }
    }


    /* 
    Hier werden die Zeitintervall Objekte erstellt und die entsprechenden API Funktionen aufgerufen. 
    Dabei wird je nach Typ des Zeitintervalls eine andere Funktion aufgerufen, die ebenfalls einen anderen Endpunkt aufruft.
    */

    addTimeIntervalBooking = () => {
        if ((this.state.type) === "vacation") {
            let newVacationBO = new VacationBO(this.state.start, this.state.end, this.state.startEvent, this.state.endEvent, this.state.type);
            WorkTimeAppAPI.getAPI().addVacationBooking(newVacationBO)
            let newBookingBO = new BookingBO(this.props.workTimeAccountId, this.props.userId, this.state.type, this.state.eventBookingId, this.state.timeintervalBookingId)
            WorkTimeAppAPI.getAPI().addBooking(newBookingBO)
            console.log(this.state.type)
            console.log(newVacationBO)
            console.log(newBookingBO)
        }
        else if ((this.state.type) === "work") {
            let newWorkBO = new WorkBO(this.state.start, this.state.end, this.state.startEvent, this.state.endEvent, this.state.type);
            WorkTimeAppAPI.getAPI().addWorkBooking(newWorkBO)
            let newBookingBO = new BookingBO(this.props.workTimeAccountId, this.props.userId, this.state.type, this.state.eventBookingId, this.state.timeintervalBookingId)
            WorkTimeAppAPI.getAPI().addBooking(newBookingBO)
            console.log(newWorkBO)
            console.log(newBookingBO)
        }
        else if ((this.state.type) === "illness") {
            let newIllnessBO = new IllnessBO(this.state.start, this.state.end, this.state.startEvent, this.state.endEvent, this.state.type);
            WorkTimeAppAPI.getAPI().addIllnessBooking(newIllnessBO)
            let newBookingBO = new BookingBO(this.props.workTimeAccountId, this.props.userId, this.state.type, this.state.eventBookingId, this.state.timeintervalBookingId)
            WorkTimeAppAPI.getAPI().addBooking(newBookingBO)
            console.log(newIllnessBO)
            console.log(newBookingBO)
        }
        else if ((this.state.type) === "projectwork") {
            let newProjectWorkBO = new ProjectWorkBO(this.state.start, this.state.end, this.state.startEvent, this.state.endEvent, this.state.type, this.state.activityId);
            WorkTimeAppAPI.getAPI().addProjectWorkBooking(newProjectWorkBO)
            let newBookingBO = new BookingBO(this.props.workTimeAccountId, this.props.userId, this.state.type, this.state.eventBookingId, this.state.timeintervalBookingId)
            WorkTimeAppAPI.getAPI().addBooking(newBookingBO)
            console.log(newProjectWorkBO)
            console.log(newBookingBO)
        }
        else if ((this.state.type) === "break") {
            let newBreakBO = new BreakBO(this.state.start, this.state.end, this.state.startEvent, this.state.endEvent, this.state.type);
            WorkTimeAppAPI.getAPI().addBreakBooking(newBreakBO)
            let newBookingBO = new BookingBO(this.props.workTimeAccountId, this.props.userId, this.state.type, this.state.eventBookingId, this.state.timeintervalBookingId)
            WorkTimeAppAPI.getAPI().addBooking(newBookingBO)
            console.log(newBreakBO)
            console.log(newBookingBO)
        }
        else if ((this.state.type) === "flexday") {
            let newFlexDayBO = new FlexDayBO(this.state.start, this.state.end, this.state.startEvent, this.state.endEvent, this.state.type);
            WorkTimeAppAPI.getAPI().addFlexDayBooking(newFlexDayBO)
            let newBookingBO = new BookingBO(this.props.workTimeAccountId, this.props.userId, this.state.type, this.state.eventBookingId, this.state.timeintervalBookingId)
            WorkTimeAppAPI.getAPI().addBooking(newBookingBO)
            console.log(newFlexDayBO)
            console.log(newBookingBO)
        }

    }

    /* 
    Hier werden die Event Objekte geholt und in der Liste vacationIllnessEvents gespeichert. 
    */
    getEventBookings = () => {
        WorkTimeAppAPI.getAPI().getVacationIllnessEventBookings(1).then(vacationBOs =>
            this.setState({
                vacationIllnessEvents: vacationBOs,
            }, function () {
                console.log(this.state.vacationIllnessEvents)
            }))
    }


    /* 
    Hier werden die Projekt Objekte geholt und in der Liste projects gespeichert. 
    */

    getProjects = () => {
        WorkTimeAppAPI.getAPI().getProjectsForUser(1).then(projectBOs =>
            this.setState({
                projects: projectBOs,
            }, function () {
                console.log(this.state.projects)
            }))
    }

    /* 
    Hier werden die Activity Objekte geholt und in der Liste activities gespeichert. 
    */
    getActivities = () => {
        if (this.state.project != null) {
            WorkTimeAppAPI.getAPI().getActivitiesByProject(this.state.project).then(activityBOs =>
                this.setState({
                    activities: activityBOs,
                }, function () {
                    console.log(this.state.activities)
                }))
        }
    }

    /* 
    Sobald die Komponenten geladen hat sollen die Events, Projekte und Aktivitäten geholt werden.
    */
    componentDidMount() {
        this.getEventBookings();
        this.getProjects();
        this.getActivities()
    }

    /* 
    Speichert den Input der Felder im state
    */

    handleChange = (e) => {
        this.setState({ [e.target.name]: e.target.value }
            , function () {
                if (this.state.project != null) {
                    this.getActivities()
                }
                console.log("ACTIVITYID", this.state.activityId)
                console.log("Menuitem", this.state.activityId)
            });
    }

    /* 
    Speichert den Input des start feldes im state
    */
    handleStartDateChange(newValue) {
        this.setState({
            start: format(new Date(newValue), "yyyy-MM-dd HH:mm:ss")
        })
        console.log(this.state.start)
    }

    /* 
    Speichert den Input des end feldes im state
    */
    handleEndDateChange(newValue) {
        this.setState({
            end: format(new Date(newValue), "yyyy-MM-dd HH:mm:ss")
        })
        console.log(this.state.end)
    }
    /* 
    Öffnen des Selects für das StartEvent
    */
    handleClickOpen = () => {
        this.setState({
            showSelectEventDialog: true
        })
    }
    /* 
    Schließen des Selects für das StartEvent
    */
    handleClose = (newEvent) => {
        if (newEvent) {
            this.setState({
                start: newEvent,
                showSelectEventDialog: false

            });
        }
        else {
            this.setState({
                showSelectEventDialog: false
            })
        }
    }


    /* 
    Öffnen des Selects für das EndEvent
    */
    handleEndClickOpen = () => {
        this.setState({
            showSelectEndEventDialog: true
        })
    }

    /* 
    Schließen des Selects für das EndEvent
    */
    handleEndClose = (newEvent) => {
        if (newEvent) {
            this.setState({
                end: newEvent,
                showSelectEndEventDialog: false

            });
        }
        else {
            this.setState({
                showSelectEndEventDialog: false
            })
        }
    }



    render() {
        return (
            <div>
                <Card sx={{ m: 5, p: 2, minwidth: 500 }}>
                    <Grid container spacing={2} sx={{ mb: 2 }} direction="row" alignItems="center">
                        <Grid item sx={{ border: 1, borderRadius: 4, ml: 2, p: 2 }}>
                            <Grid item >
                                <AccessTimeIcon ></AccessTimeIcon>
                            </Grid>
                        </Grid>
                        <Grid item xs={12} sm={4} sx={{ pb: 1 }}>
                            <Typography variant="h5" component="div">
                                Create Your Timeinterval Booking
                            </Typography>
                            <Typography sx={{ fontSize: 14 }} color="text.secondary" gutterBottom>
                                Please fill out all relevant information.
                            </Typography>
                        </Grid>
                    </Grid>
                    <Grid container spacing={2} alignItems="center">
                        <Grid item xs={12}>
                            <FormControl sx={{ minWidth: 256 }}>
                                <InputLabel>Type</InputLabel>
                                <Select
                                    name="type"
                                    value={this.state.type}
                                    label="type"
                                    onChange={this.handleChange}
                                >
                                    <MenuItem value={"work"}>Work</MenuItem>
                                    <MenuItem value={"projectwork"}>Projectwork</MenuItem>
                                    <MenuItem value={"vacation"}>Vacation</MenuItem>
                                    <MenuItem value={"illness"}>Illness</MenuItem>
                                    <MenuItem value={"break"}>Break</MenuItem>
                                    <MenuItem value={"flexday"}>Flex Days</MenuItem>
                                </Select>
                            </FormControl>
                        </Grid>
                        {/* Wenn Work, Projekt oder Break als Typ ausgewählt werden, dann soll das Grid 9 Blöcke des Screens einnehmen, sonst 3*/}
                        {(this.state.type === "" || this.state.type === "work" || this.state.type === "projectwork" || this.state.type === "break" || this.state.type === "flexday") ?
                            <Grid item xs={12} sm={9} >
                                <LocalizationProvider dateAdapter={AdapterDateFns}>
                                    <DateTimePicker
                                        renderInput={(props) => <TextField {...props} />}
                                        label="Start"
                                        value={this.state.start}
                                        onChange={(newValue) => {
                                            this.handleStartDateChange(newValue);
                                        }}
                                        minDate={new Date('2022-01-01')}
                                    />

                                </LocalizationProvider>
                            </Grid>
                            :

                            <Grid item xs={12} sm={3} >
                                <LocalizationProvider dateAdapter={AdapterDateFns}>
                                    <DateTimePicker
                                        renderInput={(props) => <TextField {...props} />}
                                        label="Start"
                                        value={this.state.start}
                                        onChange={(newValue) => {
                                            this.handleStartDateChange(newValue);
                                        }}
                                        minDate={new Date('2022-01-01')}
                                    />
                                </LocalizationProvider>

                            </Grid>}
                        {(this.state.type === "vacation" || this.state.type === "illness") ?
                            <Grid xs={12} sm={9} item>
                                <Button onClick={this.handleClickOpen} variant="contained">Select Event</Button>
                            </Grid> :
                            null}
                        {/* Wenn Work, Projekt oder Break als Typ ausgewählt werden, dann soll das Grid 9 Blöcke des Screens einnehmen, sonst 3*/}

                        {(this.state.type === "" || this.state.type === "work" || this.state.type === "projectwork" || this.state.type === "break" || this.state.type === "flexday") ?
                            <Grid xs={12} sm={9} item >
                                <LocalizationProvider dateAdapter={AdapterDateFns}>
                                    <DateTimePicker
                                        renderInput={(props) => <TextField {...props} />}
                                        label="End"
                                        value={this.state.end}
                                        onChange={(newValue) => {
                                            this.handleEndDateChange(newValue);
                                        }}
                                        minDate={new Date('2022-01-01')}
                                    />
                                </LocalizationProvider>
                            </Grid>
                            :
                            <Grid xs={12} sm={3} item >
                                <LocalizationProvider dateAdapter={AdapterDateFns}>
                                    <DateTimePicker
                                        renderInput={(props) => <TextField {...props} />}
                                        label="End"
                                        value={this.state.end}
                                        onChange={(newValue) => {
                                            this.handleEndDateChange(newValue);
                                        }}
                                        minDate={new Date('2022-01-01')}
                                    />
                                </LocalizationProvider>
                            </Grid>}
                        {(this.state.type === "vacation" || this.state.type === "illness") ?
                            <Grid xs={12} sm={9} item>
                                <Button variant="contained" onClick={this.handleEndClickOpen}>Select Event</Button>
                            </Grid> :
                            null}
                        <Grid xs={12} sm={4} item>
                            {/*
                    Wenn der Typ "Projekt" oder gewählt wurde, dann zeige auch die Felder Aktivität und Projekt an"
                    */}
                            {this.state.type === "projectwork" &&
                                <FormControl sx={{ minWidth: 256 }}>
                                    <InputLabel>Select Project</InputLabel>
                                    <Select
                                        name="project"
                                        value={this.state.project}
                                        label="project"
                                        onChange={this.handleChange}
                                    >
                                        {this.state.projects.map(projectBOs =>
                                            <MenuItem key={projectBOs.getID()} value={projectBOs.getID()}>
                                                {projectBOs.name}

                                            </MenuItem>
                                        )}
                                    </Select>
                                </FormControl>}
                        </Grid>
                        <Grid xs={12} sm={10} item>
                            {this.state.type === "projectwork" &&
                                <FormControl sx={{ minWidth: 256 }}>
                                    <InputLabel>Select Activity</InputLabel>
                                    <Select
                                        name="activityId"
                                        value={this.state.activityId}
                                        label="activity"
                                        onChange={this.handleChange}
                                    >
                                        {this.state.activities.map(activityBOs =>
                                            <MenuItem key={activityBOs.getID()} value={activityBOs.getID()}>
                                                {activityBOs.GetName()}

                                            </MenuItem>
                                        )}
                                    </Select>
                                </FormControl>}
                        </Grid>
                        <Grid xs={12} item>
                            <Button variant="contained" onClick={this.addTimeIntervalBooking}>Book Timeinterval</Button>
                        </Grid>

                    </Grid>
                </Card>

                <SelectEventDialog handleStartDateChange={this.handleStartDateChange} handlechange={this.handleChange} vacationIllnessEvents={this.state.vacationIllnessEvents} getEventBookings={this.getEventBookings} show={this.state.showSelectEventDialog} onClose={this.handleClose}></SelectEventDialog>
                <SelectEndEventDialog handleEndDateChange={this.handleEndDateChange} handlechange={this.handleChange} vacationIllnessEvents={this.state.vacationIllnessEvents} getEventBookings={this.getEventBookings} show={this.state.showSelectEndEventDialog} onClose={this.handleEndClose}></SelectEndEventDialog>

            </div>

        );
    }

}


export default TimeIntervalBookings;