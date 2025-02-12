import React from 'react';
import AccountCircleIcon from '@mui/icons-material/AccountCircle';
import PostAddIcon from '@mui/icons-material/PostAdd';
import TaskIcon from '@mui/icons-material/Task';
import WorkIcon from '@mui/icons-material/Work';
import AccessTimeIcon from '@mui/icons-material/AccessTime';
import AccessTimeFilledIcon from '@mui/icons-material/AccessTimeFilled';
import AssignmentIcon from '@mui/icons-material/Assignment';

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
        title: 'My Profile',
        path: '/myprofile',
        icon: <AccountCircleIcon />,
        className: 'nav-text'
    },
    {
        title: 'My Work Time Overview',
        path: '/individualEntry',
        icon: <AccountCircleIcon />,
        className: 'nav-text'
    },
    {
        title: 'Work Time Overview Admin',
        path: '/adminoverview',
        icon: <AccountCircleIcon />,
        className: 'nav-text'
    },
    {
        title: 'My Projects',
        path: '/myprojects',
        icon: <AssignmentIcon />,
        className: 'nav-text'
    },
    {
        title: 'Create Project',
        path: '/createprojectmain',
        icon: <TaskIcon />,
        className: 'nav-text'
    },

    {
        title: 'My Bookings',
        path: '/mybookings',
        icon: <PostAddIcon />,
        className: 'nav-text'
    },
    {
        title: 'Time Interval Bookings',
        path: '/timeintervalbookings',
        icon: <AccessTimeIcon />,
        className: 'nav-text'
    },
    {
        title: 'Event Bookings',
        path: '/eventbookings',
        icon: <AccessTimeFilledIcon />,
        className: 'nav-text'
    },

]