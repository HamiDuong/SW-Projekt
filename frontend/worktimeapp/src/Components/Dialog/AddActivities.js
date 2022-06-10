import React, { Component } from 'react';
import TextField from '@mui/material/TextField';
import Box from '@mui/material/Box';
import Button from '@mui/material/Button';
import Grid from '@mui/material/Grid'; 
import ActivityBO from '../../API/ActivityBO';
import WorkTimeAppAPI from '../../API/WorkTimeAppAPI';


class AddActivities extends Component {
    constructor(props) {
        super(props);
        this.state={
            loadingInProgress: false,
            createprojectError: null,
            activityName: null,
            capacity: null,
            activitytNameValidationFailed: false,
            activityNameEdited: false,
            capacityValidationFailed: false,
            capacityEdited: false,
            projectId: 0,
            currentCapacity: 0,
    }
    this.baseState = this.state;
}

    addActivity = () => { 
        let newActivity = new ActivityBO(this.state.activityName, this.state.capacity, this.state.projectId, this.state.currentCapacity);
        console.log(newActivity)
        WorkTimeAppAPI.getAPI().addActivity(newActivity).then(activity => {
          this.setState(this.baseState);
          this.props.onClose(activity);
        }).catch(e => 
          this.setState({
            updatingInProgress: false,
            updatingError: e
          })
          );
        this.setState({
          updatingInProgress: true,
          updatingError: null
        });
      }
    /** Handles value changes of the forms textfields and validates them */
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
           <Box
            component="form"
             sx={{
             '& > :not(style)': { m: 1, width: '25ch' },
                }}
            noValidate
            autoComplete="off">
            <div className='popup'>
                <div className='popup_inner'>
                
                <TextField type='text' required fullWidth margin='normal' id='activityName' label='activity name:' value={activityName} 
                onChange={this.textFieldValueChange} error={activityNameValidationFailed} 
                helperText={activityNameValidationFailed ? 'The activity name must contain at least one character' : ' '} />
                <TextField type='text' required fullWidth margin='normal' id='capacity' label='capacity:' value={capacity}
                onChange={this.textFieldValueChange} error={capacityValidationFailed}
                helperText={capacityValidationFailed ? 'The commissioner must contain at least one character' : ' '} />
                
                <Grid xs={12} item>
                    
                    <Button 
                    variant="contained" 
                    onClick={this.addActivity}>
                      Create Activity
                      </Button>

                    </Grid> 
                    <Grid xs={12} item>
                    <Button variant="contained" onClick={this.props.closePopupActivities}>Close</Button>
                </Grid>
                </div>
               
            </div>
             </Box>
         );
    }
}
 
export default AddActivities;