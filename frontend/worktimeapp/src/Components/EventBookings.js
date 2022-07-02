import React, { Component } from 'react';
import InputLabel from '@mui/material/InputLabel';
import MenuItem from '@mui/material/MenuItem';
import Select from '@mui/material/Select';
import TextField from '@mui/material/TextField';
import Button from '@mui/material/Button';
import EventIcon from '@mui/icons-material/Event';
import Grid from '@mui/material/Grid';
import Card from '@mui/material/Card';
import Typography from '@mui/material/Typography';
import FormControl from '@mui/material/FormControl';
import { AdapterDateFns } from '@mui/x-date-pickers/AdapterDateFns';
import { LocalizationProvider } from '@mui/x-date-pickers/LocalizationProvider';
import { DateTimePicker } from '@mui/x-date-pickers/DateTimePicker';
import VacationStartBO from '../API/EventBOs/VacationStartBO';
import VacationEndBO from '../API/EventBOs/VacationEndBO';
import IllnessStartBO from '../API/EventBOs/IllnessStartBO';
import IllnessEndBO from '../API/EventBOs/IllnessEndBO';
import ComingBO from '../API/EventBOs/ComingBO';
import GoingBO from '../API/EventBOs/GoingBO';
import WorkTimeAppAPI from '../API/WorkTimeAppAPI';
import BookingBO from '../API/BookingBO';
import { format } from "date-fns";

{/* 
@author Mihriban Dogan (https://github.com/mihriban-dogan)
EventBooking stellt die Form für Event Buchungen dar
*/}

class EventBookings extends Component {
    constructor(props) {
        super(props);
        
        this.state = {
            type: "",
            time: Date,
            workTimeAccountId:0,
            userId:1,
            eventBookingId: 0,
            timeintervalBookingId: 0,
        }
    }

    /* 
Hier werden die Event Objekte erstellt und die entsprechenden API Funktionen aufgerufen. 
Dabei wird je nach Typ des Events eine andere Funktion aufgerufen, die ebenfalls einen anderen Endpunkt aufruft.
*/

    addEventBooking = () => {
        if ((this.state.type) === "vacationBegin"){
            let newVacationBeginBO = new VacationStartBO(this.state.time);
            WorkTimeAppAPI.getAPI().addVacationBeginBooking(newVacationBeginBO)
            let newBookingBO = new BookingBO(this.state.workTimeAccountId, this.state.userId, this.state.type, this.state.eventBookingId, this.state.timeintervalBookingId)
            WorkTimeAppAPI.getAPI().addEventBooking(newBookingBO)
            console.log(this.state.type)
            console.log(newVacationBeginBO)
            console.log(newBookingBO)}

        else if ((this.state.type) === "vacationEnd"){
            let newVacationEndBO = new VacationEndBO(this.state.time);
            WorkTimeAppAPI.getAPI().addVacationEndBooking(newVacationEndBO)
            let newBookingBO = new BookingBO(this.state.workTimeAccountId, this.state.userId, this.state.type, this.state.eventBookingId, this.state.timeintervalBookingId)
            WorkTimeAppAPI.getAPI().addEventBooking(newBookingBO)
            console.log(this.state.type)
            console.log(newVacationEndBO)
            console.log(newBookingBO)}

        else if ((this.state.type) === "illnessBegin"){
            let newIllnessBeginBO = new IllnessStartBO(this.state.time);
            WorkTimeAppAPI.getAPI().addIllnessBeginBooking(newIllnessBeginBO)
            let newBookingBO = new BookingBO(this.state.workTimeAccountId, this.state.userId, this.state.type, this.state.eventBookingId, this.state.timeintervalBookingId)
            WorkTimeAppAPI.getAPI().addEventBooking(newBookingBO)
            console.log(newIllnessBeginBO)
            console.log(newBookingBO)
        }

        else if ((this.state.type) === "illnessEnd"){
            let newIllnessEndBO = new IllnessEndBO(this.state.time);
            WorkTimeAppAPI.getAPI().addIllnessEndBooking(newIllnessEndBO)
            let newBookingBO = new BookingBO(this.state.workTimeAccountId, this.state.userId, this.state.type, this.state.eventBookingId, this.state.timeintervalBookingId)
            WorkTimeAppAPI.getAPI().addEventBooking(newBookingBO)
            console.log(newIllnessEndBO)
            console.log(newBookingBO)
        }
        else if ((this.state.type) === "coming"){
            let newComingBO = new ComingBO(this.state.time);
            WorkTimeAppAPI.getAPI().addComingBooking(newComingBO)
            let newBookingBO = new BookingBO(this.state.workTimeAccountId, this.state.userId, this.state.type, this.state.eventBookingId, this.state.timeintervalBookingId)
            WorkTimeAppAPI.getAPI().addEventBooking(newBookingBO)
            console.log(newComingBO)
            console.log(newBookingBO)
        }
        else if ((this.state.type) === "going"){
            let newGoingBO = new GoingBO(this.state.time);
            WorkTimeAppAPI.getAPI().addGoingBooking(newGoingBO)
            let newBookingBO = new BookingBO(this.state.workTimeAccountId, this.state.userId, this.state.type, this.state.eventBookingId, this.state.timeintervalBookingId)
            WorkTimeAppAPI.getAPI().addEventBooking(newBookingBO)
            console.log(newGoingBO)
            console.log(newBookingBO)
        }
        
       }

    /* 
    Speichert den Input der Felder im state
    */
    handleChange = (e) =>{
        this.setState({ [e.target.name] : e.target.value });}

    handleDateChange(newValue){
        this.setState({
            time: format(new Date(newValue), "yyyy-MM-dd HH:mm:ss")
        })
        
    }

    render() { 
        return ( 
            <Card sx={{ m:5, p:2, minwidth: 500}}>
              <Grid container spacing={2} sx={{mb:2}} direction="row" alignItems="center">
                        <Grid item  sx={{border: 1, borderRadius: 4, ml:2, p:2}}>
                            <Grid item >
                                <EventIcon></EventIcon>
                            </Grid>
                        </Grid>
                        <Grid item xs={12} sm={4} sx={{pb:1}}>
                            <Typography variant="h5" component="div">
                            Create Your Event Booking
                            </Typography>
                            <Typography sx={{ fontSize: 14 }} color="text.secondary" gutterBottom>
                            Please fill out all relevant information. 
                            </Typography>
                        </Grid>
                </Grid>
                <Grid container spacing={2}  alignItems="center">
                  <Grid item xs={12}>
                       <FormControl sx={{ minWidth: 258}}>
                          <InputLabel>Type</InputLabel>
                          <Select
                            name="type"
                            value={this.state.type}
                            label="Type"
                            onChange={this.handleChange}
                          >
                            <MenuItem value={"illnessBegin"}>Illness Begin</MenuItem>
                            <MenuItem value={"illnessEnd"}>Illness End</MenuItem>
                            <MenuItem value={"vacationBegin"}>Vacation Begin</MenuItem>
                            <MenuItem value={"vacationEnd"}>Vacation End</MenuItem>
                            <MenuItem value={"coming"}>Coming</MenuItem>
                            <MenuItem value={"going"}>Going</MenuItem>
                          </Select>
                        </FormControl>
                      </Grid>
                      <Grid item xs={12} sm={12}>
                        <LocalizationProvider dateAdapter={AdapterDateFns}>
                                    <DateTimePicker
                                        renderInput={(props) => <TextField {...props} />}
                                        label="Time"
                                        value={this.state.time}
                                        onChange={(newValue) => {
                                        this.handleDateChange(newValue);
                                        }}
                                        minDate={new Date('2022-01-01')}
                                    />
                            </LocalizationProvider>
                      </Grid>
                      <Grid item xs={12} sm={2}>
                      <Button variant="contained" onClick={this.addEventBooking}>Book Event</Button>
                      </Grid>
              </Grid>
          </Card>
         );
    }
}
 
export default EventBookings;