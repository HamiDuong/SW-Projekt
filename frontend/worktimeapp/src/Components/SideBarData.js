import React from 'react';
import AccountCircleIcon from '@mui/icons-material/AccountCircle';
import PostAddIcon from '@mui/icons-material/PostAdd';
import TaskIcon from '@mui/icons-material/Task';
import WorkIcon from '@mui/icons-material/Work';
import AccessTimeIcon from '@mui/icons-material/AccessTime';
import AccessTimeFilledIcon from '@mui/icons-material/AccessTimeFilled';
import PeopleIcon from '@mui/icons-material/People';

/**
 * @author [Esra Özkul](https://github.com/EsraOEzkul)
 */
//Hier werden die Inhalte der Menüleiste erstellt.
//Title: Wie der Button heißen soll
//path: Damit wird der Pfand initialisieren
//icon: Hier werden Icons aus Material-UI angewendet
//className: Diese werden für die CSS-Datei benötigt für die Gestaltung

export const SideBarData = [
    {
        title: 'MyProfile',
        path: '/myprofile',
        icon: <AccountCircleIcon/>,
        className : 'nav-text'
    },
    {
        title: 'MyWorkTime',
        path: '/myworktime',
        icon: <WorkIcon/>,
        className : 'nav-text'
    },
    {
        title: 'MyProjects',
        path: '/myprojects',
        icon: <PeopleIcon/>,
        className : 'nav-text'
    },
    {
        title: 'CreateProjects',
        path: '/createprojects',
        icon: <TaskIcon/>,
        className : 'nav-text'
    },
    
    {
        title: 'MyBookings',
        path: '/mybookings',
        icon: <PostAddIcon/>,
        className : 'nav-text'
    },
    {
        title: 'TimeIntervalBookings',
        path: '/timeintervalbookings',
        icon: <AccessTimeIcon/>,
        className : 'nav-text'
    },
    {
        title: 'EventBookings',
        path: '/eventbookings',
        icon: <AccessTimeFilledIcon/>,
        className : 'nav-text'
    },
    {
        title: 'MyProjectsTest',
        path: '/myprojectstest',
        icon: <PeopleIcon/>,
        className : 'nav-text'
    },

    
]