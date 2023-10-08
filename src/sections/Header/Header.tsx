import HelpCenterOutlined from '@mui/icons-material/HelpCenterOutlined';
import MenuIcon from '@mui/icons-material/Menu';
import AppBar from '@mui/material/AppBar';
import Box from '@mui/material/Box';
import Button from '@mui/material/Button';
import Divider from '@mui/material/Divider';
import IconButton from '@mui/material/IconButton';
import Toolbar from '@mui/material/Toolbar';
import Tooltip from '@mui/material/Tooltip';

import { FlexBox } from '@/components/styled';
import useSidebar from '@/store/sidebar';
import S4logo from './logos/S4.svg';
import VNlogo from './logos/VN.svg';

import { ButtonGroups } from './styled';


function Header() {
  const [, sidebarActions] = useSidebar();

  return (
    <Box sx={{ flexGrow: 1 }}>
      <AppBar color="transparent" elevation={1} position="static">
        <Toolbar sx={{ justifyContent: 'space-between' }}>
          <FlexBox sx={{ alignItems: 'center' }}>
            <IconButton
              onClick={sidebarActions.toggle}
              size="large"
              edge="start"
              color="info"
              aria-label="menu"
              sx={{ mr: 1 }}
            >
              <MenuIcon />
            </IconButton>
            <Box
              component="img"
              sx={{ height: 35 }}
              alt="Logo"
              src={VNlogo}
              marginLeft='20px'
            />
              <Divider orientation="vertical" flexItem />
            <Box
              component="img"
              sx={{ height: 30 }}
              alt="Logo"
              src={S4logo}
            />
          </FlexBox>
          <FlexBox>
          <Divider orientation="vertical" flexItem />
            <ButtonGroups color='info' aria-label="outlined primary button group">
                <Tooltip title="Go to OZ1" arrow>
                    <Button href="https://oz.vnops.net/" target="_blank" rel="noreferrer">OZ1</Button>
                </Tooltip>                
                <Tooltip title="Go to OZ2" arrow>
                    <Button href="https://oz2.vnops.net/" target="_blank" rel="noreferrer">OZ2</Button>
                </Tooltip>
                <Tooltip title="Coming soon!" arrow>
                    <span>
                        <Button href="https://oz2.vnops.net/" target="_blank" rel="noreferrer" disabled={true}>OZ Next</Button>
                    </span>
                </Tooltip>
            </ButtonGroups>
            <Divider orientation="vertical" flexItem />
              <ButtonGroups color='warning' aria-label="outlined primary button group">
                  <Tooltip title="Go to Canopy | MARS DEV" arrow>
                    <Button href="https://canopy.dev.mars.vnops.net/" target="_blank" rel="noreferrer">DEV</Button>
                  </Tooltip>
                  <Tooltip title="Go to Canopy | MARS QA" arrow>
                    <Button href="https://canopy.qa.mars.vnops.net/" target="_blank" rel="noreferrer">QA</Button>
                  </Tooltip>
              </ButtonGroups>
            <Divider orientation="vertical" flexItem />
              <ButtonGroups color='success' aria-label="outlined primary button group">
                <Tooltip title="Go to Canopy | ARA PRD" arrow>
                  <Button href="https://canopy.prd.ara.vnops.net/" target="_blank" rel="noreferrer">ARA</Button>
                </Tooltip>
                <Tooltip title="Go to Canopy | CRUX PRD" arrow>
                  <Button href="https://canopy.prd.crux.vnops.net/" target="_blank" rel="noreferrer">CRUX</Button>
                </Tooltip>
                <Tooltip title="Go to Canopy | LYRA PRD" arrow>
                  <Button href="https://canopy.prd.lyra.vnops.net/" target="_blank" rel="noreferrer">LYRA</Button>
                </Tooltip>
                <Tooltip title="Go to Canopy | LEVIS PRD" arrow>
                  <Button href="https://canopy.prd.levis.vnops.net/" target="_blank" rel="noreferrer">LEVIS</Button>
                </Tooltip>
              </ButtonGroups>
            <Divider orientation="vertical" flexItem />
            <Tooltip title="Need Help?" arrow>
              <IconButton href="https://shift4.slack.com/archives/C02HK2KRL9K/" color="secondary" edge="end" size="large" >
                <HelpCenterOutlined />
              </IconButton>
            </Tooltip>
          </FlexBox>
        </Toolbar>
      </AppBar>
    </Box>
  );
}

export default Header;
