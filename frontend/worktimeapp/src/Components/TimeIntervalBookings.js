import React, { Component } from 'react';
import InputLabel from '@mui/material/InputLabel';
import MenuItem from '@mui/material/MenuItem';
import FormControl from '@mui/material/FormControl';
import Select from '@mui/material/Select';
import TextField from '@mui/material/TextField';
import Button from '@mui/material/Button';
import Grid from '@mui/material/Grid'
import Card from '@mui/material/Card';
import Typography from '@mui/material/Typography';
import AccessTimeIcon from '@mui/icons-material/AccessTime';
import { AdapterDateFns } from '@mui/x-date-pickers/AdapterDateFns';
import { LocalizationProvider } from '@mui/x-date-pickers/LocalizationProvider';
import { DateTimePicker } from '@mui/x-date-pickers/DateTimePicker';


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
            timeIntervalType: "",
            activity: "", 
            project: "",
            
         }
    }

    handleChange = (e) =>{
        this.setState({ [e.target.name] : e.target.value });}
    
    handleStartDateChange(newValue){
        this.setState({
            start: new Date(newValue)
        })
        console.log(this.state.start)
    }
    handleEndDateChange(newValue){
        this.setState({
            end: new Date(newValue)
        })
        console.log(this.state.end)
    }

    
    render() { 
        return ( 
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
                                name="timeIntervalType"
                                value={this.state.timeIntervalType}
                                label="type"
                                onChange={this.handleChange}
                            >
                                <MenuItem value={"work"}>Work</MenuItem>
                                <MenuItem value={"project"}>Project</MenuItem>
                                <MenuItem value={"vacation"}>Vacation</MenuItem>
                                <MenuItem value={"illness"}>Illness</MenuItem>
                                <MenuItem value={"flexday"}>Flexday</MenuItem>
                            </Select>
                        </FormControl>
                    </Grid>
                   {/* Wenn Work, Projekt oder Flexday als Typ ausgewählt werden, dann soll die Zeit frei wählbar sein, sonst soll die Zeit auf 24 Uhr festgelegt sein*/}
                    <Grid item xs={12} sm={2}>
                        {(this.state.timeIntervalType === "work" || this.state.timeIntervalType === "project"|| this.state.timeIntervalType === "flexday")?
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
                        <Button variant="contained">Select Event</Button>
                    </Grid> 
                     {/* Wenn Work, Projekt oder Flexday als Typ ausgewählt werden, dann soll die Zeit frei wählbar sein, sonst soll die Zeit auf 24 Uhr festgelegt sein*/}
                    <Grid xs={12} sm={2} item >
                    {(this.state.timeIntervalType === "work" || this.state.timeIntervalType === "project"|| this.state.timeIntervalType === "flexday")?
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
                        <Button variant="contained">Select Event</Button>
                    </Grid>
                    <Grid xs={12}sm={4} item>
                     {/*
                    Wenn der Typ "Projekt" oder gewählt wurde, dann zeige auch die Felder Aktivität und Projekt an"
                    */}
                    {this.state.timeIntervalType === "project" && 
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
                    {this.state.timeIntervalType === "project" &&
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
                    <Button variant="contained">Book Timeinterval</Button>
                    </Grid>

                </Grid>
                </Card>
          
         );
    }
  
}

 
export default TimeIntervalBookings;