import { Dialog } from '@headlessui/react';
import { ReactNode, useState } from 'react';
import { lazy, Suspense } from 'react-lazy-no-flicker';
import { Outlet, RouteObject, useRoutes, BrowserRouter, useNavigate } from 'react-router-dom';
import {
  LiaLightbulbSolid,
  LiaHomeSolid,
  LiaPlugSolid,
  LiaCloudUploadAltSolid,
  LiaPuzzlePieceSolid,
  LiaHistorySolid,
} from 'react-icons/lia';
import { IoShareSocialOutline, IoColorWand, IoMailOutline } from 'react-icons/io5';
import { TbChartCandleFilled, TbPlusMinus, TbReportAnalytics, TbMessage } from 'react-icons/tb';
import { GrLineChart, GrMoney } from 'react-icons/gr';
import { BsPatchExclamationFill } from 'react-icons/bs';
import { SlMagnifier } from 'react-icons/sl';
import { PiListChecksBold, PiGraphBold } from 'react-icons/pi';
import { LuLightbulb } from 'react-icons/lu';
import { NavigationProvider, useNavigation } from '~/lib/NavigationContext';
import Loadable from '../shared/Loadable';

const Loading = () => <p className="p-4 w-full h-full text-center">Loading...</p>;

const DashboardExampleScreen = Loadable(lazy(() => import('~/components/screens/DashboardExample')));
const CompanySetupScreen = Loadable(lazy(() => import('~/components/screens/CompanySetup')));
const DataConnectScreen = Loadable(lazy(() => import('~/components/screens/DataConnect')));
const DataConnectAddScreen = Loadable(lazy(() => import('~/components/screens/DataConnectAdd'))); 
const StartScreen = Loadable(lazy(() => import('~/components/screens/Start')));
const Page404Screen = Loadable(lazy(() => import('~/components/screens/404')));

interface NavigationLinkProps {
  children: ReactNode;
  stepIndex: number;
  url: string;
}
const NavigationStep: React.FC<NavigationLinkProps> = ({ url, stepIndex, children }) => {
  const { activeStep, setActiveStep, completedStep, setCompletedStep } = useNavigation();
  const navigateRouter = useNavigate();
  const navigate = (url: string) => {
    setActiveStep(stepIndex);
    navigateRouter(url);
  };

  const isActiveStep = activeStep === stepIndex;
  const isNextStep = stepIndex === completedStep + 1;
  const isCompleted = stepIndex <= completedStep;

  return (
    <li className={`step ${isNextStep ? 'step-primary' : isCompleted ? 'step-success' : ''}`}>
      <button
        className={`btn btn-block justify-start ${isCompleted ? '' : isNextStep ? 'btn-primary' : 'btn-disabled'} ${
          isActiveStep && !isNextStep ? 'btn-outline' : isNextStep ? '' : 'btn-ghost'
        }`}
        onClick={() => navigate(url)}
      >
        {children}
      </button>
    </li>
  );
};

function Layout() {
  return (
    <div className="drawer min-h-screen bg-base-200 lg:drawer-open">
      <input id="my-drawer" type="checkbox" className="drawer-toggle" />
      <main className="drawer-content">
        <Outlet />
      </main>
      <aside className="drawer-side z-40" style={{ scrollBehavior: 'smooth', scrollPaddingTop: '5rem' }}>
        <label htmlFor="my-drawer" className="drawer-overlay"></label>
        <nav className="flex min-h-screen w-200 flex-col gap-2 overflow-y-auto bg-base-100 px-6 py-10">
          <div className="mx-4 flex items-center gap-2 font-black">INTRIQ</div>
          <ul className="steps steps-vertical">
            <NavigationStep url="/setup-company" stepIndex={1}>
              <LiaHomeSolid /> Setup Company
            </NavigationStep>
            <NavigationStep url="/connect-data" stepIndex={2}>
              <LiaPlugSolid /> Connect Data
            </NavigationStep>
            <NavigationStep url="/discover-insights" stepIndex={3}>
              <PiGraphBold /> Discover Insights
            </NavigationStep>
            <NavigationStep url="/track" stepIndex={4}>
              <GrLineChart /> Track
            </NavigationStep>
            <NavigationStep url="/dashboard-example" stepIndex={5}>
              <GrLineChart /> Dashboard
            </NavigationStep>
          </ul>
        </nav>
      </aside>
    </div>
  );
}

export const Router = () => {
  return (
    <BrowserRouter>
      <NavigationProvider>
        <InnerRouter />
      </NavigationProvider>
    </BrowserRouter>
  );
};

const InnerRouter = () => {
  const routes: RouteObject[] = [
    {
      path: '/',
      element: <Layout />,
      children: [
        {
          index: true,
          element: <StartScreen />,
        },
        {
          path: '/setup-company',
          element: <CompanySetupScreen />,
        },
        {
          path: '/connect-data',
          children: [
            {
              path: '/connect-data/add',
              element: <DataConnectAddScreen />,
            },
            {
              path: '/connect-data',
              element: <DataConnectScreen />,
            }
          ]
        },
        {
          path: '/track',
          element: <StartScreen />,
        },
        {
          path: '/dashboard-example',
          element: <DashboardExampleScreen />,
        },
        {
          path: '*',
          element: <Page404Screen />,
        },
      ],
    },
  ];
  const element = useRoutes(routes);
  return (
    <div>{element}</div>
  );
};
