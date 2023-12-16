import { Head } from '~/components/shared/Head';
import '~/../node_modules/react-vis/dist/style.css';
import { useNavigation } from '~/lib/NavigationContext';
import Navbar from '../shared/Navbar';
import ReactFlow, {
  Node,
  Edge,
  useNodesState,
  useEdgesState,
  OnSelectionChangeParams,
  Controls,
  useReactFlow,
  ReactFlowProvider,
  Background,
  BackgroundVariant,
} from 'reactflow';
import { useEffect, useState } from 'react';
import { FlexibleXYPlot, LineSeries, XAxis, YAxis } from 'react-vis';
import { IoIosArrowUp, IoIosArrowDown } from "react-icons/io";

import 'reactflow/dist/style.css';
import { AnimationDefinition, motion } from 'framer-motion';

const dummydata = [
  { x: 0, y: 2 },
  { x: 1, y: 5 },
  { x: 2, y: 4 },
  { x: 3, y: 6 },
  { x: 4, y: 1 },
  { x: 5, y: 3 },
  { x: 6, y: 6 },
  { x: 7, y: 5 },
  { x: 8, y: 7 },
  { x: 9, y: 9 },
];

function InsightDiscovery() {
  const { completedStep, setCompletedStep, activeStep, setActiveStep } = useNavigation();
  const { getNode } = useReactFlow();

  const [detailsFull, setDetailsFull] = useState<boolean>(false);
  const [navbarTitle, setNavbarTitle] = useState<string>('Discover Insights');
  const [selectedNodeId, setSelectedNodeId] = useState<string | null>(null);
  const [selectedNodeLabel, setSelectedNodeLabel] = useState<string | null>(null);
  const onSelectionChangeHandler = (props: OnSelectionChangeParams) => {
    const { nodes } = props;
    if (nodes.length !== 0) {
      setSelectedNodeId(nodes[0].id);
      setSelectedNodeLabel(nodes[0].data.label);
    } else {
      setSelectedNodeId(null);
    }
  };

  useEffect(() => {
    setActiveStep(3);
  }, []);

  const initialNodes: Node<NodeData>[] = [
    { id: '1', position: { x: 0, y: 0 }, data: { label: 'Revenue', type: 'FinancialMetric' } },
    { id: '2', position: { x: 100, y: -50 }, data: { label: 'Online Sales Growth', type: 'OperationalMetric' } },
    { id: '3', position: { x: 100, y: 50 }, data: { label: 'Customer Footfall', type: 'ValueLever' } },
  ];

  const initialEdges: Edge<EdgeData>[] = [
    { id: '1->2', source: '1', target: '2' },
    { id: '2->3', source: '2', target: '3' },
    { id: '3->1', source: '3', target: '1' },
  ];

  const [nodes, setNodes, onNodesChange] = useNodesState<NodeData>(initialNodes);
  const [edges, setEdges, onEdgesChange] = useEdgesState<EdgeData>(initialEdges);

  type NodeType = 'FinancialMetric' | 'OperationalMetric' | 'ValueLever';
  type NodeData = { label: string; type: NodeType };
  type EdgeData = {};

  const detailsVariants = {
    hidden: {
      top: '100%',
    },
    open: {
      top: 'calc(100% - 5rem)',
    },
    full: {
      top: 'calc(0% - 4rem)',
    },
  };

  const buttonVariants = {
    hidden: {
      top: '0',
    },
    open: {
      top: '-1rem',
    },
    full: {
      top: '+4rem',
    },
  };

  function onAnimationComplete(definition: AnimationDefinition): void {
    if (definition == 'full') {
      setNavbarTitle(getNode(selectedNodeId!)?.data.label);
    } else setNavbarTitle('Discover Insights');
  }

  function handleOnClick(): void {
    if (completedStep < 3) setCompletedStep(3);
  }

  return (
    <>
      <Head title="Discover Insights" />
      <Navbar title={navbarTitle} />
      <div className="bg-base-300 relative w-full overflow-hidden" style={{ height: 'calc(100% - 4rem)' }}>
        <ReactFlow
          nodes={nodes}
          edges={edges}
          onNodesChange={onNodesChange}
          onEdgesChange={onEdgesChange}
          onSelectionChange={onSelectionChangeHandler}
          selectNodesOnDrag={true}
          proOptions={{ hideAttribution: true }}
          preventScrolling={false}
          fitView
        >
          <Controls showInteractive={true} position="top-right" />
          <Background color="#ccc" variant={BackgroundVariant.Dots} />
        </ReactFlow>
        <motion.div
        initial={'hidden'}
        animate={selectedNodeId ? (detailsFull ? 'full' : 'open') : 'hidden'}
        variants={detailsVariants}
        onAnimationComplete={onAnimationComplete}
        className="absolute bg-base-200 w-full top-[100%] flex flex-col p-6 pt-3 pr-0 overflow-visible"
        style={{ height: 'calc(100% + 4rem)' }}
      >
        <h1 className="lg:text-2xl lg:font-light">{selectedNodeLabel}</h1>
        <p>3% p.a.</p>
        <span className='pb-3'></span>
        <div className='pr-6 overflow-y-scroll'>
          <div className="grid grid-cols-12 grid-rows-[min-content] gap-y-12 lg:gap-x-12">
            <section className="card col-span-12 bg-base-100 shadow-sm xl:col-span-6 min-h-[300px]">
              <div className="card-body pb-0">
                <h2 className="card-title">19,000</h2>
                <p>Downloads</p>
              </div>
              <FlexibleXYPlot>
                <XAxis />
                <YAxis />
                <LineSeries data={dummydata} />
              </FlexibleXYPlot>
            </section>
            <section className="card col-span-12 bg-base-100 shadow-sm xl:col-span-6 min-h-[300px]">
              <div className="card-body pb-0">
                <h2 className="card-title">19,000</h2>
                <p>Downloads</p>
              </div>
              <FlexibleXYPlot>
                <XAxis />
                <YAxis />
                <LineSeries data={dummydata} />
              </FlexibleXYPlot>
            </section>
            <section className="card col-span-12 bg-base-100 shadow-sm xl:col-span-6 min-h-[300px]">
              <div className="card-body pb-0">
                <h2 className="card-title">19,000</h2>
                <p>Downloads</p>
              </div>
              <FlexibleXYPlot>
                <XAxis />
                <YAxis />
                <LineSeries data={dummydata} />
              </FlexibleXYPlot>
            </section>
            <button className='btn btn-primary col-span-8' onClick={() => handleOnClick()}>Track Initiative</button>
          </div>
        </div>
        <motion.button
          animate={selectedNodeId ? (detailsFull ? 'full' : 'open') : 'hidden'}
          variants={buttonVariants}
          className="btn btn-sm btn-primary absolute"
          style={{left: 'calc(50% - 50px)'}}
          onClick={() => {setDetailsFull((value) => !value);}}
        >
          {detailsFull ? <><IoIosArrowDown /> Show less</> : <><IoIosArrowUp /> Show more</>}
        </motion.button>
      </motion.div>
      </div>
    </>
  );
}

export default () => {
  return (
    <ReactFlowProvider>
      <InsightDiscovery />
    </ReactFlowProvider>
  );
};
