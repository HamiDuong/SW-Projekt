import { Dialog, DialogActions, DialogContent, DialogTitle, paperClasses, TextField } from '@mui/material';
import { pickersDayClasses } from '@mui/x-date-pickers/PickersDay/pickersDayClasses';
import React, { Component } from 'react';
import ProjectBO from '../API/ProjectBO';
import WorkTimeAppAPI from '../API/WorkTimeAppAPI';
import Box from '@mui/material/Box';
//import TextField from '@mui/material/TextField';
import Button from '@mui/material/Button';
import Grid from '@mui/material/Grid'; 
import AddActivities from './Dialog/AddActivities'

class CreateProject extends Component {
    constructor(props) {
        super(props);
        this.state={
            showPopup: false
        }
    }
    togglePopup() {
        this.setState({
          showPopup: !this.state.showPopup
        });
      }
    
    render() { 
        
        return ( 
    <Box
      component="form"
      sx={{
        '& > :not(style)': { m: 1, width: '25ch' },
      }}
      noValidate
      autoComplete="off"
    >

      <TextField id="outlined-basic" label="Name" variant="outlined" />
      <br/>
      <TextField id="outlined-basic" label="Commissoner" variant="outlined" />
      
      <br/>
      <TextField
        id="startfilter"
        label="Duration Start"
        variant="standard"
        format={'YYYY/MM/DD'}
        type = "date"
        InputLabelProps={{
            shrink: true,
                        }}
        />
        <br/>
        <TextField
        id="startfilter"
        label="Duration Ende"
        variant="standard"
        format={'YYYY/MM/DD'}
        type = "date"
        InputLabelProps={{
            shrink: true,
                        }}
        />
        <Grid xs={12} item>
                    <Button variant="contained" onClick={this.addProject}>Create Project</Button>
        </Grid>
        <Grid xs={12} item>
                    <Button variant="contained" onClick={this.togglePopup.bind(this)}>AddActivities</Button>
        </Grid>
        {this.state.showPopup ? 
          <AddActivities
            text='Close Me'
            closePopup={this.togglePopup.bind(this)}
          />
          : null
        }

        
    </Box>

    )
    }
}
 
export default CreateProject;