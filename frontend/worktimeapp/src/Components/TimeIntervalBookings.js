import React, { Component } from 'react';
import InputLabel from '@mui/material/InputLabel';
import MenuItem from '@mui/material/MenuItem';
import FormControl from '@mui/material/FormControl';
import Select from '@mui/material/Select';
import TextField from '@mui/material/TextField';
import Button from '@mui/material/Button';
import { withStyles} from '@mui/styles';
import Grid from '@mui/material/Grid'
import Card from '@mui/material/Card';
import Typography from '@mui/material/Typography';
import AccessTimeIcon from '@mui/icons-material/AccessTime';


class TimeIntervalBookings extends Component {
    constructor(props) {
        super(props);
       
        this.state = { 
            start: "",
            end: "",
            timeIntervalType: "",
            activity: "", 
            project: ""
         }
    }

    handleChange = (e) =>{
        this.setState({ [e.target.name] : e.target.value });}

    
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
                   
                    <Grid item xs={4} sm={2}>
                        <TextField name="startdate" label="Start date" variant="outlined" />
                    </Grid>
                   
                    <Grid xs={4} sm={2} item>
                        {(this.state.timeIntervalType == "work" || this.state.timeIntervalType=="project"|| this.state.timeIntervalType=="flexday") && 
                        <TextField name="starttime" label="Start time" variant="outlined" />
                        }
                    </Grid>
                    <Grid xs={4} sm={8} item>
                        <Button variant="contained">Select Event</Button>
                    </Grid>
                    <Grid xs={4} sm={2} item >
                        <TextField name="enddate" label="End date" variant="outlined" />
                    </Grid>
                    <Grid xs={4}  sm={2} item>
                        {(this.state.timeIntervalType == "work" || this.state.timeIntervalType=="project" || this.state.timeIntervalType=="flexday") && 
                        <TextField name="endtime" label="End time" variant="outlined" />
                        }
                    </Grid>
                    <Grid xs={4}  sm={8} item>
                        <Button variant="contained">Select Event</Button>
                    </Grid>
                    <Grid xs={12}sm={2} item>
                    {this.state.timeIntervalType == "project" && 
                    <FormControl sx={{ minWidth: 220}}>
                            <InputLabel>Project</InputLabel>
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
                    {this.state.timeIntervalType == "project" &&
                    <FormControl sx={{ minWidth: 220}}>
                            <InputLabel>Activity</InputLabel>
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

const styles = theme => ({
  });
 
export default withStyles(styles)(TimeIntervalBookings);