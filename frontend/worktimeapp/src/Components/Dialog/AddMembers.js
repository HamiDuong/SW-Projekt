import React, { Component } from 'react';
import WorkTimeAppAPI from '../../API/WorkTimeAppAPI';
import ProjectUserBO from '../../API/ProjectUserBO';
import { Box } from '@mui/system';
import Select from '@mui/material/Select';
import { Button, IconButton, Dialog, DialogContent, DialogTitle, TextField, Typography, InputAdornment, MenuItem, DialogActions, Grid } from '@mui/material';
import SearchIcon from '@mui/icons-material/Search';
import Card from '@mui/material/Card';


/**
 * @author [Esra Özkul](https://github.com/EsraOEzkul)
 */
/**
 * Hier werden die einzelnen Members für die Projekte hinzugefügt.
 */

class AddMembers extends Component {
  constructor(props) {
    super(props);
      this.state={
      projectId: '',
      userId: 1,
      capacity: 0,
      users: [],
      userName:'',
      targetusers: [],
      selecteduserName: null,
      loadingInProgress: false,
      userNameSearchError: null,
      userNotFound: false,
      selectedUser: null,
      currentCapacity: 0, 
      capacityValidationFailed: false,
      open: false,
      }
  
  }
  
  /** In dieser Funktion kann man die einzelnen User mit der Nachname suchen. */
  searchUserNamesForProject = async () => {
    const {userName} = this.state;
    console.log(this.state.userName);
    if (userName.length > 0) {
      try {
        this.setState({
          targetuserName: [],
          selectedUser: null,
          loadingInProgress:true,
          userNameSearchError: null
        });

        //Jetzt werden die User geladen.
        const users = await WorkTimeAppAPI.getAPI().searchUser(userName);
        console.log("Test");
      let selectedUser = null;

      if(users.length > 0) {
        selectedUser = users[0];
      } else {
        this.setState({
          userNotFound: true
        });
      }
      //Hier wird der endgültiger Zustand gesetzt.
      this.setState({
        targetusers: users,
        selectedUser: selectedUser,
        loadingInProgress: false,
        userNameSearchError: null,

      }, function(){
        console.log("State", this.state.targetusers)
      });
    } catch (e) {
      this.setState({
        targetusers: [],
        selectedUser: null,
        loadingInProgress: false,
        userNameSearchError: e

      });
    }
    }
  }
    /** Verwaltet Wertänderungen des Users select-Textfeldes */
  userSelectionChange = (event) => {
    let users = event.target.value;
    
    this.setState({
      selectedUser: users,
    });
  }
  
  /** Behandelt Wertänderungen der Formular-Textfelder und validiert diese */ 
  textFieldValueChange = (event) => {
    const val = event.target.value;
    // Validate the amount field
    this.setState({
      [event.target.id]: val
    });
  }
  
  handle(e) {
    this.setState({
    event: e.target.value,
    selectedUser: true,
    userId: e.target.value
            
    }, console.log(this.state.userId));
  }

  /* 
  Sobald die Komponenten geladen hat soll die Funktion searchUserNamesForProject geholt werden.
  */
  componentDidMount() {
    this.searchUserNamesForProject(1);
  } 

  addProjectUser = () => { 
    let newProjectUser = new ProjectUserBO(this.props.projectId, this.state.selectedUser.getID(), this.state.capacity, this.state.currentCapacity);
    console.log(newProjectUser);
    WorkTimeAppAPI.getAPI().addProjectUser(newProjectUser).then(projectuser => 
      this.setState({
        projectId: projectuser.project_id,
        capacity: projectuser.capacity,
        userId: projectuser.userId,
        currentCapacity: projectuser.currentCapacity
      }, 
        function(){
        console.log('Here', projectuser, this.state.projectId, this.state.capacity)
         }))
      alert("Member added");
  }

  /** Verwaltet das Schliessen / Abbrechen-Klickereignis */
  handleClose = () => {
    this.props.closePopupMembers();
  }

  state = {  }
  render() { 
    const users = this.props;
    const {userName, targetuserName, selecteduserName, userNameSearchError, loadingInProgress, targetusers, searchUser, selectedUser, capacity,capacityValidationFailed} = this.state;
    return ( 
      <Card sx={{ m:1, p:3, minwidth: 700}}>
        <Box>
          <form noValidate autoComplete='off'>
              {
                // Zeigt eine Auswahl von targetUsers an, falls vorhanden. Geben Sie keine Suchschaltfläche.
                (targetusers.length === 0) ? 
                  <TextField autoFocus fullWidth margin='normal' type='text' required id='userName' label='user name:'
                    onChange={this.textFieldValueChange}
                    onBlur={this.searchUserNamesForProject}
                    InputProps={{
                      endAdornment: <InputAdornment position='end'>
                        <IconButton onClick={this.searchUserNamesForProject}>
                          <SearchIcon />
                        </IconButton>
                      </InputAdornment>,
                    }} />
                  :
                  // Zeigt eine Auswahl von selectedUser an, falls vorhanden. Geben Sie keine Suchschaltfläche.
                  <TextField select autoFocus fullWidth margin='normal' type='text' required id='userName' label='user name:'
                    value={selectedUser}
                    onChange={this.userSelectionChange}>
                    {
                      targetusers.map((users) => (

                        <MenuItem key={users.getID()} value={users}>
                          {users.getLastName()}, {users.getFirstName()}
                        </MenuItem>
                      ))
                    }
                  </TextField>
                  
              }
              </form>
              <TextField type='text' required fullWidth margin='normal' id='capacity' label='capacity:' value={capacity}
                onChange={this.textFieldValueChange} error={capacityValidationFailed}
                helperText={capacityValidationFailed ? 'The commissioner must contain at least one character' : ' '} />
                
              
              <Button disabled={!selectedUser} variant='contained' onClick={this.addProjectUser} color='secondary'>
                add new member
              </Button>
              <Button onClick={this.handleClose} color='secondary'>
                Cancel
              </Button>
        </Box>
      </Card>
     );
  }
}
 
export default AddMembers;