import React, { Component } from 'react';
import AssignmentIcon from '@mui/icons-material/Assignment';

import {withStyles,
    Typography,
    Accordion,
    AccordionSummary,
    AccordionDetails,
    TextField,
    Button,
    List,
    ListItem,
    Box,
    Collapse,
    ListItemText,
    ListItemIcon,
    ListItemButton,
    ListSubheader,
    TableRow,
    TableHead,
    TableContainer,
    TableCell,
    TableBody,
    Table,
    Paper,
    FormControl,
    Card,
    Grid,
    Select,
    MenuItem,
    InputLabel
} from '@mui/material';

import { MyProjectpopup } from './MyProjectpopup';
import EditActivity from './Dialog/EditActivity';
import MyActivitiesEntry from './MyActivitiesEntry'
import WorkTimeAppAPI from '../API/WorkTimeAppAPI';
import EditProject from './Dialog/EditProject';
import AddActivity from './Dialog/AddActivity';
import { isThursday } from 'date-fns';

const header = [
  {
  id: 'name',
  name: 'Name',
  label: 'Name'
  },
  {
      id: 'commissioner',
      name: 'Commissioner',
      label: 'Commissioner'
  }, 
  {
      id: 'user',
      name: 'User',
      label: 'User'
  },
  {
      id: 'duration',
      name: 'Duration',
      label: 'Duration'
  },
]
const data = [
  {
      id: 1,
      name:'SW Project',
      commissioner: 'Thies',
      user: 'Susi',
      duration: '90 Tage'
  },
  {
      id: 2,
      name:'Programmieren',
      commissioner: 'Thies',
      user: 'Susi',
      duration: '999 Tage'
  },
  {
      id: 3,
      name:'Schlafen',
      commissioner: '',
      user: 'Susi',
      duration: '15 Tage'
  }
]

const activities = [
    {
        name: "Use Case erstellen",
        capacity: "45h"
    },
    {
        name: "ERM Diagram",
        capacity: "10h"
    },
    {
        name: "Blabla",
        capacity: "5h"
    },
]

/**
 * Projekte und Activities vom aktuellen User
 * 
 * @author [Vi Nam Le] (https://github.com/vinamle)
 */

class MyProjects extends Component {
    
    constructor(props) {
        super(props);

        this.state = {
          userId : props.userId,
          projects : null,
          projectuser: null,

          showEditWindow: false,
          showEditActicity: false,

          workTimeAccountId:0,
          // userId: 1,
          showEditProject: false,

          showAddActivity: false,
          selectedProjectId: null,
      }
  }

  // editWindow = () => {
  //   this.setState({
  //     showEditWindow: true
  //   }, function(){
  //     console.log('Edit Window öffnen')
  //   })
  // }

  // closeDialog = (project) => {
  //   this.setState({
  //     showEditWindow:false
  //   }, function(){
  //     console.log('Edit Window schließen')
  //   })
    
  // }

  // editWindowActivity = () => {
  //   this.setState({
  //     showEditActicity: true
  //   }, function(){
  //     console.log('Edit Window')
  //   })
  // }

  // closeDialogActivity = (activity) => {
  //   if(activity){
  //     this.updateProject(activity)
  //     this.setState({
  //       showEditActicity: false
  //     }, function(){
  //       console.log('Edit Window')
  //     })
  //   }else{
  //     this.setState({
  //       showEditWindow:false
  //     }, function(){
  //       console.log('Edit Window')
  //     })
  //   }
  // }

  //ProjectUser BOs von User holen -> damit Projekte holen
  getProjects = () => {
    // WorkTimeAppAPI.getAPI().getProjectUserByUserId(this.state.userId).then(projectuser =>   
    //   this.setState({
    //     projectuser : projectuser
    //   }, function(){
    //     console.log("API ProjectUser")
    //   })  
    // )
    
    // let resproject = []

    // this.state.projectuser.forEach(elem => {
    //   WorkTimeAppAPI.getAPI().getProject(elem.getProjectId()).then(project =>
    //     resproject.append(project)
    //   )
    // });

    // this.setState({
    //   projects : resproject
    // }, function(){
    //   console.log('Got the new projects')
    // })

    WorkTimeAppAPI.getAPI().getProjectsByProjectUser(this.state.userId).then(project =>
      this.setState({
        projects : project
      }, function(){
        console.log("Projekte wurden geholt", project[0])
        this.state.projects.forEach(function(elem){
          console.log(elem)
        })
      })
    )

  }

  // updateProject = (project) => {
  // }

  // openEditProjectWindow = () => {
  //   this.setState({
  //     showEditProject: true
  //   }, function(){
  //     console.log('Edit Window Projekt öffnen')
  //   })

  //   console.log(this.state.showEditProject)
  // }

  // closeEditProjectWindow = () => {
  //     this.setState({
  //       showEditProject:false
  //     }, function(){
  //       console.log('Edit Window Projekt schließen')
  //     })
  // }

  // openAddActivityWindow = () => {
    // if(item.userId == this.state.userId){
    //   this.setState({
    //     showAddActivity: true
    //   }, function(){
    //     console.log('Add Activity Window öffnen')
    //   })  
    //   console.log(this.state.showEditProject)
    // }else{
    //   console.log('Hallo')
    // }
    
  //     this.setState({
  //       showAddActivity: true,
      
  //     }, function(){
  //       console.log('Add Activity Window öffnen')
  //     })  
  //     console.log(this.state.showEditProject)
    
  // }

  // closeAddActivityWindow = () => {
  //     this.setState({
  //       showAddActivity:false
  //     }, function(){
  //       console.log('Add Activity Window schließen')
  //     })
  // }

  componentDidMount(){
    this.getProjects();
    console.log("Component Did Mount", this.state.projects)
    
  }

  projectDeleted = project => {
    const newProjectList = this.state.projects.filter(projectFromState => projectFromState.getID() !== project);
    console.log(project)
    this.setState({
      projects: newProjectList,
    });
  }

  render(){
    const {projects} = this.state
    if(projects==null){
      return null
    }
    return(
      <Card sx={{ m:5, p:2, minwidth: 500}}>
        <Typography variant="h5" component="div">
          <AssignmentIcon></AssignmentIcon>
          My Projects
        </Typography>
        <Typography sx={{ fontSize: 16 }} color="text.secondary" gutterBottom>
          Your projects and activities at the moment. 
        </Typography>

        {projects.map((item) => (
          <Accordion>
            <AccordionSummary>
              <TableRow>
                <TableCell>
                  {"Project name: "+item.name}
                </TableCell>
                <TableCell align="right">
                  {"Commisioner: "+item.commissioner}
                </TableCell>
              </TableRow>
            </AccordionSummary>
            <AccordionDetails>
              <Table>
                <TableHead>
                  <TableRow>
                    <TableCell>Activities</TableCell>
                    <TableCell align="left">Capacity</TableCell>
                    <TableCell></TableCell>
                    <TableCell></TableCell>
                  </TableRow>
                </TableHead>
                <TableBody>
                <MyActivitiesEntry key = {item.getID()} onProjectDeleted={this.projectDeleted} projectId = {item.id} userId={this.state.userId} admin = {item.userId} project = {item}></MyActivitiesEntry> 
                </TableBody>
              </Table>
              {/* <MyProjectpopup show={this.state.showEditWindow} onClose={this.closeDialog} project={item}></MyProjectpopup> */}
              {/* <Button onClick = {this.openEditProjectWindow}>Edit Project</Button>
              <Button id = 'addActivity' onClick = {this.openAddActivityWindow} project = {item}>Add Activity</Button> */}
            </AccordionDetails>
            {/* <EditProject show={this.state.showEditProject} project = {item} onClose={this.closeEditProjectWindow}></EditProject>
            <AddActivity show = {this.state.showAddActivity} project = {item} onClose = {this.closeAddActivityWindow}></AddActivity> */}
          </Accordion>
        ))}
      </Card>
    )
  }
}
export default MyProjects