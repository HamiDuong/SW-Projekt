import React, { Component } from 'react';
import Box from '@mui/material/Box';
import TextField from '@mui/material/TextField';
import Button from '@mui/material/Button';
import WorkTimeAppAPI from './../API/WorkTimeAppAPI';
import UserBO from '../API/UserBO';

class MyProfile extends Component {
    constructor(props) {
      super(props)
      this.state = {
          id:0,
      dateOfLastChange : 0,
       first_name:"",
       last_name:"",
       mail_adress:"",
       user_name:"",
       updatingError: null,
       updatingInProgress: false,  
      }
    }
    componentDidMount(){
        WorkTimeAppAPI.getAPI().getUserByID(this.state.id).then(respons=>{
            this.setState({
                id:respons.id,
                dateOfLastChange:respons.dateOfLastChange,
                first_name:respons.first_name,
                last_name:respons.last_name,
                mail_adress:respons.mail_adress,
                user_name:respons.user_name,
                updatingInProgress: false,
            })
        }).catch(e =>
            this.setState({
              updatingInProgress: false,    // disable loading indicator 
              updatingError: e              // show error message
            })
          );
      
          // set loading to true
          this.setState({
            updatingInProgress: true,       // show loading indicator
            updatingError: null             // disable error message
          });
    }
    handleSave(){
        const {id, dateOfLastChange, first_name, last_name, mail_adress, user_name} =this.state
        var user=UserBO(first_name, last_name, mail_adress, user_name)
        user.setID(id)
        user.setDateOfLastChange(dateOfLastChange)
        WorkTimeAppAPI.getAPI().updateUser(this.state.id,user).then(respons=>{
            this.setState({
                id:respons.id,
                dateOfLastChange:respons.dateOfLastChange,
                first_name:respons.first_name,
                last_name:respons.last_name,
                mail_adress:respons.mail_adress,
                user_name:respons.user_name,
                updatingInProgress: false,
            })
        }).catch(e =>
            this.setState({
              updatingInProgress: false,    // disable loading indicator 
              updatingError: e              // show error message
            })
          );
      
          // set loading to true
          this.setState({
            updatingInProgress: true,       // show loading indicator
            updatingError: null             // disable error message
          });
    }

 

    render() { 
        const {first_name, last_name, mail_adress, user_name} =this.state
        return (
        <Box
            component="form"
            sx={{'& > :not(style)': { m: 1, width: '25ch' }, }}
            noValidate
            autoComplete="off"
            >
            <TextField id="first_name" label="Outlined" variant="outlined" value={first_name} onChange={this.handleNameChange}/>
            <TextField id="last_name" label="Outlined" variant="outlined" value={last_name} onChange={(e)=>{this.setState({last_name:e.target.value})}}/>
            <TextField id="mail_adress" label="Outlined" variant="outlined" value={mail_adress} onChange={(e)=>{this.setState({mail_adress:e.target.value})}}/>
            <TextField id="user_name" label="Outlined" variant="outlined" value={user_name} onChange={(e)=>{this.setState({user_name:e.target.value})}}/>
            <Button variant="outlined" onClick={this.handleNameChange}>Speichern</Button>
            </Box>
        )

    }
}
 
export default MyProfile;
