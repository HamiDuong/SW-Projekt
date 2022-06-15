import { Dialog, DialogActions, DialogContent, DialogTitle, paperClasses, TextField } from '@mui/material';
import { pickersDayClasses } from '@mui/x-date-pickers/PickersDay/pickersDayClasses';
import React, { Component } from 'react';
import ProjectBO from '../API/ProjectBO';
import WorkTimeAppAPI from '../API/WorkTimeAppAPI';
import Box from '@mui/material/Box';
import Button from '@mui/material/Button';
import Grid from '@mui/material/Grid';
import AddActivities from './Dialog/AddActivities';
import AddMember from './Dialog/AddMembers';
import PropTypes from 'prop-types';
import Typography from '@mui/material/Typography';

class CreateProject extends Component {
  constructor(props) {
    super(props);

    this.state = {
      showPopupActivity: false,
      showPopupMember:false,
      //Network states
      loadingInProgress: false,
      createprojectError: null,
      projectName: null,
      commissioner: null,
      userid: 0,
      members: [],
      showAddMember: false,
      userName: '',
      targetMember: [],
      selectedMember: null,
      projectId: '',

    }
    this.baseState = this.state;

  }
  handleChange() {
    this.props.onChange()
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

  componentDidMount() {
    console.log(this.props.selected)
  }

  showing() {
    if (this.props.selected) {
      return (
        <div>
          <Grid xs={12} item>
            <Button variant="contained" onClick={() => this.setState({ showPopupActivity: true })}>Add Activity</Button>
          </Grid>

          {
            this.state.showPopupActivity?
              <AddActivities
                projectId={this.props.value}
                text='Close Me'
                closePopupActivities={() => this.setState({ showPopupActivity: false })}
              />
              : null}
              
            <Grid xs={12} item>
            <Button variant="contained" onClick={() => this.setState({ showPopupMember: true })}>Add Members</Button>
            </Grid>
            {
            this.state.showPopupMember?
              <AddMember
                projectId={this.props.value}
                text='Close Me'
                closePopupMembers={() => this.setState({ showPopupMember: false })}
              />
              : null}

          


        </div >
      )
    } else {
      return <h1>You need to create a Project to add activities</h1>
    }
  }
  render() {
    const showing = this.showing()
    const { classes } = this.props;
    const { projectName, projectNameValidationFailed, commissioner, commissionerValidationFailed } = this.state
    return (
      <Box
        component="form"
        sx={{
          '& > :not(style)': { m: 1, width: '25ch' },
        }}
        noValidate
        autoComplete="off"
      >

        {/* <Grid xs={12} item>
          <Button variant="contained" onClick={this.togglePopupMembers.bind(this)}>+</Button>
        </Grid>


        {this.state.showPopupAddMembers ?
          <AddMember
            text='Close Me'
            closePopupMembers={this.togglePopupMembers.bind(this)}
          />
          : null
        } */}

        {showing}

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