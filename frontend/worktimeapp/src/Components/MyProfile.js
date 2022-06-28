import React, { Component } from 'react';
import InputLabel from '@mui/material/InputLabel';
import TextField from '@mui/material/TextField';
import Button from '@mui/material/Button';
import Grid from '@mui/material/Grid'; 
import Card from '@mui/material/Card';
import Typography from '@mui/material/Typography';
import AccountCircleIcon from '@mui/icons-material/AccountCircle';
import DeleteProfile from './DeleteProfile';
import EditProfile from './EditProfile.js'
import WorkTimeAppAPI from '../API/WorkTimeAppAPI';






{/* 
@author Mihriban Dogan 
TimeIntervalBooking stellt die Form für Zeitintervall Buchungen dar
"""*/}


class TimeIntervalBookings extends Component {
    constructor(props) {
        super(props);
       
        this.state = { 
            workTimeAccountId:0,
            userId: 1,
            showSelectEventDialog: false,
            showSelectEndEventDialog: false,
            firstName: "", 
            lastName:"",
            mailAdress:"",
            showDeleteProfile: false,
            showEditProfile: false,
            currentUser: null,
           
            
         }
    }

    


    componentDidMount() {
        this.getUser(this.props.user.uid);
   }

//    setUser = () =>{
//     this.setState({
//        mailAdress: this.props.user.email, 
//         })
   
//    }

    handleChange = (e) =>{
        this.setState({ [e.target.name] : e.target.value });}
    
   

    handleDeleteClickOpen = () => {
        this.setState({
            showDeleteProfile: true
        })
      }
   
    
    handleDeleteClose = () =>{
            this.setState({
              showDeleteProfile: false

            });
        }


    handleEditClickOpen = () => {
        this.setState({
            showEditProfile: true
        })
      }
    handleEditClose = (firstName, lastName, updatedUserBO) =>{
        if (firstName, lastName)
            this.setState({
            firstName: firstName,
            lastName: lastName,
            currentUser: updatedUserBO,
            showEditProfile: false
            })
        else{
            this.setState({
                showEditProfile: false
            })
        }
        }

    getUser = (id) => {
        WorkTimeAppAPI.getAPI().getUserByGoogleUserId(id).then(userBO =>
            this.setState({  
                firstName: userBO[0].getFirstName(),
                lastName: userBO[0].getLastName(),
                mailAdress: this.props.user.email,
                currentUser: userBO[0]
            }, function(){
                console.log(this.state.currentUser)
            }))
    }
      

    

    
    render() { 
        return ( 
            <div>
            <Card sx={{ m:5, p:2, minwidth: 500}}>
                <Grid container spacing={2} sx={{mb:2}} direction="row" alignItems="center">
                        <Grid item  sx={{border: 1, borderRadius: 4, ml:2, p:2}}>
                            <Grid item >
                                <AccountCircleIcon></AccountCircleIcon>
                            </Grid>
                        </Grid>
                        <Grid item xs={12} sm={4} sx={{pb:1}}>
                            <Typography variant="h5" component="div">
                            Profile
                            </Typography>
                            <Typography sx={{ fontSize: 14 }} color="text.secondary" gutterBottom>
                            Edit or Delete your profile. 
                            </Typography>
                        </Grid>
                        <Grid item xs={12} sm={12} sx={{pb:1}}>
                        <TextField onChange={this.handleChange} name="firstName" label="first name" value={this.state.firstName} InputProps={{readOnly: true}} variant="outlined" />
                        </Grid>
                        <Grid item xs={12} sm={12} sx={{pb:1}}>
                        <TextField  onChange={this.handleChange} name="lastName" label="last name"value={this.state.lastName} InputProps={{readOnly: true}} variant="outlined" />
                        </Grid>
                        <Grid item xs={12} sm={12} sx={{pb:1}}>
                        <TextField label="email" variant="outlined" value= {this.state.mailAdress} InputProps={{readOnly: true}} />
                        </Grid>
                        <Grid item xs={12} sm={1} sx={{pb:1}}>
                        <Button variant="contained" onClick={this.handleEditClickOpen} >Edit </Button>
                        </Grid>
                        <Grid item xs={12} sm={1} sx={{pb:1}}>
                        <Button variant="contained" color="error" onClick={this.handleDeleteClickOpen}>Delete</Button>
                        </Grid>
                </Grid>
            </Card>
            <DeleteProfile show={this.state.showDeleteProfile} onClose={this.handleDeleteClose} currentUser = {this.state.currentUser}/>
            <EditProfile show={this.state.showEditProfile} onClose={this.handleEditClose} currentUser = {this.state.currentUser} />

                
            </div>
          
         );
    }
  
}

 
export default TimeIntervalBookings;