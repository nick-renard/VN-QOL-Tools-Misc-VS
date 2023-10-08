import AddTaskIcon from '@mui/icons-material/AddTask';
import BugReportIcon from '@mui/icons-material/BugReport';
import GitHubIcon from '@mui/icons-material/GitHub';
import Terminal from '@mui/icons-material/Terminal';
import HomeIcon from '@mui/icons-material/Home';
import TerrainIcon from '@mui/icons-material/Terrain';

import asyncComponentLoader from '@/utils/loader';

import { Pages, Routes } from './types';
import { HelpOutline } from '@mui/icons-material';

const routes: Routes = {
  [Pages.Welcome]: {
    component: asyncComponentLoader(() => import('@/pages/Welcome')),
    path: '/',
    title: 'Welcome',
    icon: HomeIcon,
  },
  [Pages.QOLScripts]: {
    component: asyncComponentLoader(() => import('@/pages/QOLScripts')),
    path: '/QOLScripts',
    title: 'QOL Scripts',
    icon: Terminal,
  },
  [Pages.FAQ]: {
    component: asyncComponentLoader(() => import('@/pages/FAQ')),
    path: '/FAQ',
    title: 'FAQ',
    icon: HelpOutline,
  },
  // [Pages.Page3]: {
  //   component: asyncComponentLoader(() => import('@/pages/Page3')),
  //   path: '/page-3',
  //   title: 'Page 3',
  //   icon: TerrainIcon,
  // },
  // [Pages.Page4]: {
  //   component: asyncComponentLoader(() => import('@/pages/Page4')),
  //   path: '/page-4',
  //   title: 'Page 4',
  //   icon: BugReportIcon,
  // },
  [Pages.NotFound]: {
    component: asyncComponentLoader(() => import('@/pages/NotFound')),
    path: '*',
  },
};

export default routes;
