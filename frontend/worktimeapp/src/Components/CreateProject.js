import { Dialog, DialogActions, DialogContent, DialogTitle, paperClasses, TextField } from '@mui/material';
import { pickersDayClasses } from '@mui/x-date-pickers/PickersDay/pickersDayClasses';
import React, { Component } from 'react';
import ProjectBO from '../API/ProjectBO';
import WorkTimeAppAPI from '../API/WorkTimeAppAPI';
import Box from '@mui/material/Box';
//import TextField from '@mui/material/TextField';
import Button from '@mui/material/Button';
import Grid from '@mui/material/Grid'; 
import AddActivities from './Dialog/AddActivities';
import AddMember from './Dialog/AddMembers';
import PropTypes from 'prop-types';

class CreateProject extends Component {
    constructor(props) {
        super(props);
        // let pn = '', cm = '';
        // if (props.project) {
        //   pn = props.project.GetName();
        //   cm = props.project.GetCommisioner();
        this.state={
            showPopupAddActivities: false,
            showPopupAddMembers: false,
          //Network states
            loadingInProgress: false,
            createprojectError: null,
            projectName: null,
            commissioner: null,
            projectNameValidationFailed: false,
            projectNameEdited: false,
            commissionerValidationFailed: false,
            commissionerEdited: false,
            userid: 0

        }
        this.baseState = this.state;
        
    }
    togglePopupActivities() {
        this.setState({
          showPopupAddActivities: !this.state.showPopupAddActivities,
        });
      }
    
    togglePopupMembers() {
        this.setState({
          showPopupAddMembers: !this.state.showPopupAddMembers,
        });
      }

    addProjects = () => { 
      let newProject = new ProjectBO(this.state.projectName, this.state.commissioner, this.state.userid);
      console.log(newProject)
      WorkTimeAppAPI.getAPI().addProject(newProject).then(project => {
        this.setState(this.baseState);
        this.props.onClose(project);
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
      const {classes} = this.props; 
      const {projectName, projectNameValidationFailed, commissioner, commissionerValidationFailed} = this.state     
        return ( 
    <Box
      component="form"
      sx={{
        '& > :not(style)': { m: 1, width: '25ch' },
      }}
      noValidate
      autoComplete="off"
    > 
              <TextField type='text' required fullWidth margin='normal' id='projectName' label='project name:' value={projectName} 
                onChange={this.textFieldValueChange} error={projectNameValidationFailed} 
                helperText={projectNameValidationFailed ? 'The project name must contain at least one character' : ' '} />
              <TextField type='text' required fullWidth margin='normal' id='commissioner' label='commissioner:' value={commissioner}
                onChange={this.textFieldValueChange} error={commissionerValidationFailed}
                helperText={commissionerValidationFailed ? 'The commissioner must contain at least one character' : ' '} />
              

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
                    <Button variant="contained" onClick={this.togglePopupActivities.bind(this)}>+</Button>
        </Grid>
        
        {this.state.showPopupAddActivities ? 
          <AddActivities
            text='Close Me'
            closePopupActivities={this.togglePopupActivities.bind(this)}
          />
          : null
        }
        

        <Grid xs={12} item>
                    <Button variant="contained" onClick={this.togglePopupMembers.bind(this)}>+</Button>
        </Grid>
        

        {this.state.showPopupAddMembers ? 
          <AddMember
            text='Close Me'
            closePopupMembers={this.togglePopupMembers.bind(this)}
          />
          : null
        }

        <Grid xs={12} item>
                    <Button 
                    variant="contained" 
                    onClick={this.addProjects}>
                      Create Project
                      </Button>
        </Grid>   

        
    </Box>

    )
    }
}
/** PropTypes */
CreateProject.propTypes = {
  /** @ignore */
  classes: PropTypes.object.isRequired,
  /** The CustomerBO to be edited */
  customer: PropTypes.object,
  /** If true, the form is rendered */
  show: PropTypes.bool.isRequired,
  /**  
   * Handler function which is called, when the dialog is closed.
   * Sends the edited or created CustomerBO as parameter or null, if cancel was pressed.
   *  
   * Signature: onClose(CustomerBO customer);
   */
  onClose: PropTypes.func.isRequired,
}
 
export default CreateProject;