import React, { Component } from 'react';
import WorkTimeAppAPI from '../../API/WorkTimeAppAPI';
import ProjectUserBO from '../../API/ProjectUserBO';
import { Box } from '@mui/system';
import Select from '@mui/material/Select';
import { Button, IconButton, Dialog, DialogContent, DialogTitle, TextField, Typography, InputAdornment, MenuItem, DialogActions, Grid } from '@mui/material';
import SearchIcon from '@mui/icons-material/Search';

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
  }
  
     }
  searchUserNamesForProject = async () => {
    const {userName} = this.state;
    console.log(this.state.userName)
    if (userName.length > 0) {
      try {
        this.setState({
          targetuserName: [],
          selectedUser: null,
          loadingInProgress:true,
          userNameSearchError: null
        });

        //Jetzt werden die User geladen
        const users = await WorkTimeAppAPI.getAPI().searchUser(userName);
        console.log("Test")
      let selectedUser = null;

      if(users.length > 0) {
        selectedUser = users[0];
      } else {
        this.setState({
          userNotFound: true
        });
      }
      //set the final state
      this.setState({
        targetusers: users,
        selectedUser: selectedUser,
        loadingInProgress: false,
        userNameSearchError: null
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
    }}
    /** Handles value changes of the customer select textfield */
  userSelectionChange = (event) => {
    let users = event.target.value;

    this.setState({
      selectedUser: users,
    });
  }

  
    /** Handles value changes of the forms textfields and validates the transferAmout field */
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
  
       componentDidMount() {
        this.searchUserNamesForProject(1)
       } 

       addProjectUser = () => { 
        let newProjectUser = new ProjectUserBO(this.props.projectId, this.state.userId, this.state.capacity, this.state.currentCapacity);
        console.log(newProjectUser)
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
      }
      /** Handles the close / cancel button click event */
      handleClose = () => {
        this.props.onClose(null);
      }

  state = {  }
  render() { 
    const users = this.props;
    const {userName, targetuserName, selecteduserName, userNameSearchError, loadingInProgress, targetusers, searchUser, selectedUser} = this.state;
    return ( 
      <Box>

            <form noValidate autoComplete='off'>
              {
                // show a search text field if there are no searchedCustomer yet
                (targetusers.length === 0) ? 
                  <TextField autoFocus fullWidth margin='normal' type='text' required id='userName' label='User name:'
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
                  // Show a selection of targetCustomers, if there are any. Provide no search button. 
                  <TextField select autoFocus fullWidth margin='normal' type='text' required id='userName' label='Customer name:'
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
              
              <Button disabled={!selectedUser} variant='contained' color='primary' onClick={this.addProjectUser}>
              add new member
              </Button>
                {/* <Select onChange={this.handleChange}>
                    {users.map(project =>
                        users.map(elem => <MenuItem value={elem.id}>{elem.name}</MenuItem>)
                    )}
                </Select> */}
                
            </Box>
     );
  }
}
 
export default AddMembers;