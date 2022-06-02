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
import VacationBO from '../API/VacationBO';
import IllnessBO from '../API/IllnessBO'
import WorkBO from '../API/WorkBO'
import BookingBO from '../API/BookingBO';
import BreakBO from '../API/BreakBO';
import ProjectWorkBO from '../API/ProjectWorkBO';
import WorkTimeAppAPI from '../API/WorkTimeAppAPI';
import { format } from "date-fns";


{/* 
@author Mihriban Dogan 
TimeIntervalBooking stellt die Form für Zeitintervall Buchungen dar
"""*/}


class TimeIntervalBookings extends Component {
    constructor(props) {
        super(props);
       
        this.state = { 
            start: Date,
            end: Date,
            type: "",
            activity: "", 
            project: "",
            startEvent: null,
            endEvent: null,
            workTimeAccountId:0,
            userId: 1,
            showSelectEventDialog: false,
            eventBookingId: 0,
            timeintervalBookingId: 0,
            activityId: 0,
            
         }
    }

    addTimeIntervalBooking = () => {
        if ((this.state.type) === "vacation"){
            let newVacationBO = new VacationBO(this.state.start, this.state.end, this.state.startEvent, this.state.endEvent, this.state.type);
            WorkTimeAppAPI.getAPI().addVacationBooking(newVacationBO)
            let newBookingBO = new BookingBO(this.state.workTimeAccountId, this.state.userId, this.state.type, this.state.eventBookingId, this.state.timeintervalBookingId)
            WorkTimeAppAPI.getAPI().addBooking(newBookingBO)
            console.log(this.state.type)
            console.log(newVacationBO)
            console.log(newBookingBO)}
        else if ((this.state.type) === "work"){
            let newWorkBO = new WorkBO(this.state.start, this.state.end, this.state.startEvent, this.state.endEvent, this.state.type);
            WorkTimeAppAPI.getAPI().addWorkBooking(newWorkBO)
            let newBookingBO = new BookingBO(this.state.workTimeAccountId, this.state.userId, this.state.type, this.state.eventBookingId, this.state.timeintervalBookingId)
            WorkTimeAppAPI.getAPI().addBooking(newBookingBO)
            console.log(newWorkBO)
            console.log(newBookingBO)
        }
        else if ((this.state.type) === "illness"){
            let newIllnessBO = new IllnessBO(this.state.start, this.state.end, this.state.startEvent, this.state.endEvent, this.state.type);
            WorkTimeAppAPI.getAPI().addIllnessBooking(newIllnessBO)
            let newBookingBO = new BookingBO(this.state.workTimeAccountId, this.state.userId, this.state.type, this.state.eventBookingId, this.state.timeintervalBookingId)
            WorkTimeAppAPI.getAPI().addBooking(newBookingBO)
            console.log(newIllnessBO)
            console.log(newBookingBO)
        }
        else if ((this.state.type) === "projectwork"){
            let newProjectWorkBO = new ProjectWorkBO(this.state.start, this.state.end, this.state.startEvent, this.state.endEvent, this.state.type, this.state.activityId);
            WorkTimeAppAPI.getAPI().addProjectWorkBooking(newProjectWorkBO)
            let newBookingBO = new BookingBO(this.state.workTimeAccountId, this.state.userId, this.state.type, this.state.eventBookingId, this.state.timeintervalBookingId)
            WorkTimeAppAPI.getAPI().addBooking(newBookingBO)
            console.log(newProjectWorkBO)
            console.log(newBookingBO)
        }
        else if ((this.state.type) === "break"){
            let newBreakBO = new BreakBO(this.state.start, this.state.end, this.state.startEvent, this.state.endEvent, this.state.type);
            WorkTimeAppAPI.getAPI().addBreakBooking(newBreakBO)
            let newBookingBO = new BookingBO(this.state.workTimeAccountId, this.state.userId, this.state.type, this.state.eventBookingId, this.state.timeintervalBookingId)
            WorkTimeAppAPI.getAPI().addBooking(newBookingBO)
            console.log(newBreakBO)
            console.log(newBookingBO)
        }
       }



    handleChange = (e) =>{
        this.setState({ [e.target.name] : e.target.value });}
    
    handleStartDateChange(newValue){
        this.setState({
            start: format(new Date(newValue), "yyyy-MM-dd HH:mm:ss")
        })
        console.log(this.state.start)
    }
    handleEndDateChange(newValue){
        this.setState({
            end: format(new Date(newValue), "yyyy-MM-dd HH:mm:ss")
        })
        console.log(this.state.end)
    }

    handleClickOpen = () => {
        this.setState({
            showSelectEventDialog: true
        })
      }
    
    handleClose = () =>{
        this.setState({
            showSelectEventDialog: false
        })
      }
    

    
    render() { 
        return ( 
            <div>
            <Card sx={{ m:5, p:2, minwidth: 500}}>
                <Grid container spacing={2} sx={{mb:2}} direction="row" alignItems="center">
                        <Grid item  sx={{border: 1, borderRadius: 4, ml:2, p:2}}>
                            <Grid item >
                                <AccessTimeIcon ></AccessTimeIcon>
                            </Grid>
                        </Grid>
                        <Grid item xs={12} sm={4} sx={{pb:1}}>
                            <Typography variant="h5" component="div">
                            Create Your Timeinterval Booking
                            </Typography>
                            <Typography sx={{ fontSize: 14 }} color="text.secondary" gutterBottom>
                            Please fill out all relevant information. 
                            </Typography>
                        </Grid>
                </Grid>
                <Grid container spacing={2}  alignItems="center">
                    <Grid item xs={12}>
                        <FormControl sx={{ minWidth: 220}}>
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
                                <MenuItem value={"flexdays"}>Flex Days</MenuItem>
                            </Select>
                        </FormControl>
                    </Grid>
                   {/* Wenn Work, Projekt oder Break als Typ ausgewählt werden, dann soll die Zeit frei wählbar sein, sonst soll die Zeit auf 24 Uhr festgelegt sein*/}
                    <Grid item xs={12} sm={2} >
                        {(this.state.type === "work" || this.state.type === "projectwork"|| this.state.type === "break" || this.state.type === "flexdays")?
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
                            </LocalizationProvider> :

                             <LocalizationProvider dateAdapter={AdapterDateFns}>
                             <DateTimePicker
                                 renderInput={(props) => <TextField {...props} />}
                                 label="Start"
                                 value={this.state.start}
                                 onChange={(newValue) => {
                                 this.handleStartDateChange(newValue);
                                 }}
                                 minDate={new Date('2022-01-01')}
                                 minTime={new Date(0, 0, 0, 12)}
                                 maxTime={new Date(0, 0, 0, 12, 1)
                                }
                             />
                         </LocalizationProvider>
                        }
                    </Grid>
                    <Grid xs={12} sm={10} item>
                        <Button onClick={this.handleClickOpen} variant="contained">Select Event</Button>
                    </Grid> 
                     {/* Wenn Work, Projekt oder Break als Typ ausgewählt werden, dann soll die Zeit frei wählbar sein, sonst soll die Zeit auf 24 Uhr festgelegt sein*/}
                    <Grid xs={12} sm={2} item >
                    {(this.state.type === "work" || this.state.type === "projectwork"|| this.state.type === "break")?
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
                        </LocalizationProvider>:
                        <LocalizationProvider dateAdapter={AdapterDateFns}>
                            <DateTimePicker
                                renderInput={(props) => <TextField {...props} />}
                                label="End"
                                value={this.state.end}
                                onChange={(newValue) => {
                                this.handleEndDateChange(newValue);
                                }}
                                minDate={new Date('2022-01-01')}
                                minTime={new Date(0, 0, 0, 12, 0)}
                                maxTime={new Date(0, 0, 0, 12, 1)
                                }
                                
                            />
                        </LocalizationProvider>}
                    </Grid>
                    <Grid xs={12}  sm={8} item>
                        <Button variant="contained" onClick={this.handleClickOpen}>Select Event</Button>
                    </Grid>
                    <Grid xs={12}sm={4} item>
                     {/*
                    Wenn der Typ "Projekt" oder gewählt wurde, dann zeige auch die Felder Aktivität und Projekt an"
                    */}
                    {this.state.type === "projectwork" && 
                    <FormControl sx={{ minWidth: 220}}>
                            <InputLabel>Select Project</InputLabel>
                            <Select
                                name="project"
                                value={this.state.project}
                                label="project"
                                onChange={this.handleChange}
                            >
                                <MenuItem value={"tbd"}>TBD</MenuItem>
                            </Select>
                        </FormControl>}
                    </Grid>
                    <Grid xs={12} sm={10} item>
                    {this.state.type === "projectwork" &&
                    <FormControl sx={{ minWidth: 220}}>
                            <InputLabel>Select Activity</InputLabel>
                            <Select
                                name="activity"
                                value={this.state.activity}
                                label="activity"
                                onChange={this.handleChange}
                            >
                                <MenuItem value={"tbd"}>TBD</MenuItem>
                            </Select>
                        </FormControl>}
                    </Grid>
                    <Grid xs={12} item>
                    <Button variant="contained" onClick={this.addTimeIntervalBooking}>Book Timeinterval</Button>
                    </Grid>

                </Grid>
                </Card>

                <SelectEventDialog show={this.state.showSelectEventDialog} onClose={this.handleClose}></SelectEventDialog>
            </div>
          
         );
    }
  
}

 
export default TimeIntervalBookings;