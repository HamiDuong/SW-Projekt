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

/**
 * @author [Esra Özkul](https://github.com/EsraOEzkul)
 */
/**
 * Hier werden die beiden Dialoge aufgerufen AddActivities und AddMembers.
 */
class CreateProject extends Component {
  constructor(props) {
    super(props);

    this.state = {
      showPopupActivity: false,
      showPopupMember:false,
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
      users: props.users,
      showAddProjectMember: false,

    }
    this.baseState = this.state;

  }
  handleChange() {
    this.props.onChange()
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


  componentDidMount() {
    console.log(this.props.selected)
  }

  /** Sobald der Button 'Create Project' geklickt wird, öffnen sie weitere zwei Buttons 'Add Activity' und 'Add Members'
   * Wenn man auf die jeweilige Button klickt öffnet sich der dazugehörige PopUp.
   */
  showing() {
    if (this.props.selected) {
      return (
        <div>
          <Grid xs={12} item>
            <Button onClick={() => this.setState({ showPopupActivity: true })}>Add Activity</Button>
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
            <Button onClick={() => this.setState({ showPopupMember: true })}>Add Members</Button>
            </Grid>
            {
            this.state.showPopupMember?
              <AddMember
                users = {this.props.users}
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
    /** Hier wird die Funktion showing in die Konstante gesetzt. */
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
        {/** Hier wird die funktion showing aufgerufen */}
        {showing}

      </Box>

    )
  }
}

export default CreateProject;