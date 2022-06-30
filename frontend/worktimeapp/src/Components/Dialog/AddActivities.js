import React, { Component } from 'react';
import TextField from '@mui/material/TextField';
import Box from '@mui/material/Box';
import Button from '@mui/material/Button';
import Grid from '@mui/material/Grid'; 
import ActivityBO from '../../API/ActivityBO';
import WorkTimeAppAPI from '../../API/WorkTimeAppAPI';
import { Dialog, DialogActions, DialogContent, DialogTitle, IconButton} from '@mui/material';
import CloseIcon from '@mui/icons-material/Close';
import Card from '@mui/material/Card';

/**
 * @author [Esra Özkul](https://github.com/EsraOEzkul)
 */

/**
 * Hier werden die Aktivitäten für das Projekt erstellt.
 */

class AddActivities extends Component {
    constructor(props) {
        super(props);
        this.state={
            activityName: null,
            capacity: null,
            activitytNameValidationFailed: false,
            activityNameEdited: false,
            capacityValidationFailed: false,
            capacityEdited: false,
            projectId: '',
            currentCapacity: 0,
    }
    this.baseState = this.state;
}

    /* 
    Hier werden die Aktivitäten Objekte erstellt und die entsprechenden API Funktionen aufgerufen. 
    */
    addActivity = () => { 
        let newActivity = new ActivityBO(this.state.activityName, this.state.capacity, this.props.projectId, this.state.currentCapacity);
        console.log(newActivity)
        WorkTimeAppAPI.getAPI().addActivity(newActivity).then(activity => 
         this.setState({
          activityName:activity.name,
          capacity: activity.capacity,
          currentCapacity: activity.currentCapacity,
          projectId: activity.project_id
         }, 
         function(){
          console.log('Here', activity, this.state.projectId, this.state.activityName)
         }))
    }
    
    /** Behandelt Wertänderungen der Formular-Textfelder und validiert diese */
    textFieldValueChange = (event) => {
        const value = event.target.value;
    
        let error = false;
        if (value.trim().length === 0) {
          error = true;
        }
    
        this.setState({
          [event.target.id]: event.target.value,
          [event.target.id + 'ValidationFailed']: error,
          [event.target.id + 'Edited']: true
        });
    }
    
    render() { 
        const {activityName, activityNameValidationFailed, capacity, capacityValidationFailed} = this.state 
        return ( 
            <Card sx={{ m:1, p:3, minwidth: 700}}>
           <Box
            component="form"
            noValidate
            autoComplete="off">
            <div className='popup'>
                <div className='popup_inner'>
                    
                {/**Hier befinden sich die TextFields für das befüllen der Values, die später in der Funktion addProject aufgerufen werden. */}
                <TextField type='text' required fullWidth margin='normal' id='activityName' label='activity name:' value={activityName} 
                onChange={this.textFieldValueChange} error={activityNameValidationFailed} 
                helperText={activityNameValidationFailed ? 'The activity name must contain at least one character' : ' '} />
                <TextField type='text' required fullWidth margin='normal' id='capacity' label='capacity:' value={capacity}
                onChange={this.textFieldValueChange} error={capacityValidationFailed}
                helperText={capacityValidationFailed ? 'The commissioner must contain at least one character' : ' '} />
                
                <Grid xs={12} item>
                    
                    <Button 
                    variant="contained" 
                    onClick={this.addActivity}
                    color='secondary'>
                      Create Activity
                      </Button>
                    
                </Grid> 
                <br/>

                    <Grid xs={12} item>
                    <Button onClick={this.props.closePopupActivities} color='secondary'>Cancel</Button>
                </Grid>
                </div>
               
            </div>
            </Box>
            </Card>
        );
    }
}

 
export default  AddActivities;
