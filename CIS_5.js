/************** 
 * Cis_5 Test *
 **************/

import { PsychoJS } from './lib/core-2021.1.4.js';
import * as core from './lib/core-2021.1.4.js';
import { TrialHandler } from './lib/data-2021.1.4.js';
import { Scheduler } from './lib/util-2021.1.4.js';
import * as visual from './lib/visual-2021.1.4.js';
import * as sound from './lib/sound-2021.1.4.js';
import * as util from './lib/util-2021.1.4.js';
//some handy aliases as in the psychopy scripts;
const { abs, sin, cos, PI: pi, sqrt } = Math;
const { round } = util;

// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color([0, 0, 0]),
  units: 'height',
  waitBlanking: true
});

// store info about the experiment session:
let expName = 'CIS_5';  // from the Builder filename that created this script
let expInfo = {'participant': '', 'session': '001'};

// Start code blocks for 'Before Experiment'
// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); }, flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
flowScheduler.add(ConsentRoutineBegin());
flowScheduler.add(ConsentRoutineEachFrame());
flowScheduler.add(ConsentRoutineEnd());
flowScheduler.add(WelcomeRoutineBegin());
flowScheduler.add(WelcomeRoutineEachFrame());
flowScheduler.add(WelcomeRoutineEnd());
flowScheduler.add(InstructionRoutineBegin());
flowScheduler.add(InstructionRoutineEachFrame());
flowScheduler.add(InstructionRoutineEnd());
const trials_7LoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trials_7LoopBegin, trials_7LoopScheduler);
flowScheduler.add(trials_7LoopScheduler);
flowScheduler.add(trials_7LoopEnd);
flowScheduler.add(Interruption1RoutineBegin());
flowScheduler.add(Interruption1RoutineEachFrame());
flowScheduler.add(Interruption1RoutineEnd());
const trialsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trialsLoopBegin, trialsLoopScheduler);
flowScheduler.add(trialsLoopScheduler);
flowScheduler.add(trialsLoopEnd);
flowScheduler.add(Interruption1RoutineBegin());
flowScheduler.add(Interruption1RoutineEachFrame());
flowScheduler.add(Interruption1RoutineEnd());
const trials_2LoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trials_2LoopBegin, trials_2LoopScheduler);
flowScheduler.add(trials_2LoopScheduler);
flowScheduler.add(trials_2LoopEnd);
flowScheduler.add(Interruption1RoutineBegin());
flowScheduler.add(Interruption1RoutineEachFrame());
flowScheduler.add(Interruption1RoutineEnd());
const trials_3LoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trials_3LoopBegin, trials_3LoopScheduler);
flowScheduler.add(trials_3LoopScheduler);
flowScheduler.add(trials_3LoopEnd);
flowScheduler.add(Interruption1RoutineBegin());
flowScheduler.add(Interruption1RoutineEachFrame());
flowScheduler.add(Interruption1RoutineEnd());
const trials_4LoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trials_4LoopBegin, trials_4LoopScheduler);
flowScheduler.add(trials_4LoopScheduler);
flowScheduler.add(trials_4LoopEnd);
flowScheduler.add(Interruption1RoutineBegin());
flowScheduler.add(Interruption1RoutineEachFrame());
flowScheduler.add(Interruption1RoutineEnd());
const trials_5LoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trials_5LoopBegin, trials_5LoopScheduler);
flowScheduler.add(trials_5LoopScheduler);
flowScheduler.add(trials_5LoopEnd);
flowScheduler.add(EndAndDebriefRoutineBegin());
flowScheduler.add(EndAndDebriefRoutineEachFrame());
flowScheduler.add(EndAndDebriefRoutineEnd());
flowScheduler.add(quitPsychoJS, '', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, '', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  resources: [
    {'name': 'pattern/group 43/4304.jpg', 'path': 'pattern/group 43/4304.jpg'},
    {'name': 'pattern/group 16/1602.jpg', 'path': 'pattern/group 16/1602.jpg'},
    {'name': 'pattern/group 41/4101.jpg', 'path': 'pattern/group 41/4101.jpg'},
    {'name': 'pattern/group 41/4103.jpg', 'path': 'pattern/group 41/4103.jpg'},
    {'name': 'pattern/group 44/4401.jpg', 'path': 'pattern/group 44/4401.jpg'},
    {'name': 'pattern/group 5/0501.jpg', 'path': 'pattern/group 5/0501.jpg'},
    {'name': 'pattern/group 16/1604.jpg', 'path': 'pattern/group 16/1604.jpg'},
    {'name': 'pattern/group 34/3401.jpg', 'path': 'pattern/group 34/3401.jpg'},
    {'name': 'pattern/group 40/4002.jpg', 'path': 'pattern/group 40/4002.jpg'},
    {'name': 'pattern/group 46/4602.jpg', 'path': 'pattern/group 46/4602.jpg'},
    {'name': 'pattern/group 38/3803.jpg', 'path': 'pattern/group 38/3803.jpg'},
    {'name': 'pattern/group 17/1702.jpg', 'path': 'pattern/group 17/1702.jpg'},
    {'name': 'pattern/group 36/3602.jpg', 'path': 'pattern/group 36/3602.jpg'},
    {'name': 'pattern/group 39/3903.jpg', 'path': 'pattern/group 39/3903.jpg'},
    {'name': 'Stimuli/stimuli_9.jpeg', 'path': 'Stimuli/stimuli_9.jpeg'},
    {'name': 'pattern/group 46/4601.jpg', 'path': 'pattern/group 46/4601.jpg'},
    {'name': 'pattern/group 25/2501.jpg', 'path': 'pattern/group 25/2501.jpg'},
    {'name': 'pattern/group 42/4203.jpg', 'path': 'pattern/group 42/4203.jpg'},
    {'name': 'pattern/group 50/5004.jpg', 'path': 'pattern/group 50/5004.jpg'},
    {'name': 'pattern/group 39/3901.jpg', 'path': 'pattern/group 39/3901.jpg'},
    {'name': 'pattern/group 45/4501.jpg', 'path': 'pattern/group 45/4501.jpg'},
    {'name': 'pattern/group 24/2403.jpg', 'path': 'pattern/group 24/2403.jpg'},
    {'name': 'pattern/group 32/3202.jpg', 'path': 'pattern/group 32/3202.jpg'},
    {'name': 'pattern/group 5/0504.jpg', 'path': 'pattern/group 5/0504.jpg'},
    {'name': 'pattern/group 12/1201.jpg', 'path': 'pattern/group 12/1201.jpg'},
    {'name': 'pattern/group 40/4003.jpg', 'path': 'pattern/group 40/4003.jpg'},
    {'name': 'pattern/group 7/0703.jpg', 'path': 'pattern/group 7/0703.jpg'},
    {'name': 'pattern/group 26/2604.jpg', 'path': 'pattern/group 26/2604.jpg'},
    {'name': 'pattern/group 22/2204.jpg', 'path': 'pattern/group 22/2204.jpg'},
    {'name': 'pattern/group 32/3204.jpg', 'path': 'pattern/group 32/3204.jpg'},
    {'name': 'pattern/group 15/1501.jpg', 'path': 'pattern/group 15/1501.jpg'},
    {'name': 'pattern/group 48/4802.jpg', 'path': 'pattern/group 48/4802.jpg'},
    {'name': 'pattern/group 1/0103.jpg', 'path': 'pattern/group 1/0103.jpg'},
    {'name': 'pattern/group 18/1804.jpg', 'path': 'pattern/group 18/1804.jpg'},
    {'name': 'pattern/group 23/2302.jpg', 'path': 'pattern/group 23/2302.jpg'},
    {'name': 'pattern/group 8/0801.jpg', 'path': 'pattern/group 8/0801.jpg'},
    {'name': 'pattern/group 44/4404.jpg', 'path': 'pattern/group 44/4404.jpg'},
    {'name': 'pattern/group 34/3404.jpg', 'path': 'pattern/group 34/3404.jpg'},
    {'name': 'pattern/group 26/2602.jpg', 'path': 'pattern/group 26/2602.jpg'},
    {'name': 'pattern/group 35/3502.jpg', 'path': 'pattern/group 35/3502.jpg'},
    {'name': 'pattern/group 11/1101.jpg', 'path': 'pattern/group 11/1101.jpg'},
    {'name': 'pattern/group 14/1401.jpg', 'path': 'pattern/group 14/1401.jpg'},
    {'name': 'pattern/group 38/3804.jpg', 'path': 'pattern/group 38/3804.jpg'},
    {'name': 'pattern/group 45/4504.jpg', 'path': 'pattern/group 45/4504.jpg'},
    {'name': 'pattern/group 32/3201.jpg', 'path': 'pattern/group 32/3201.jpg'},
    {'name': 'pattern/group 46/4604.jpg', 'path': 'pattern/group 46/4604.jpg'},
    {'name': 'pattern/group 19/1904.jpg', 'path': 'pattern/group 19/1904.jpg'},
    {'name': 'pattern/group 27/2703.jpg', 'path': 'pattern/group 27/2703.jpg'},
    {'name': 'pattern/group 29/2903.jpg', 'path': 'pattern/group 29/2903.jpg'},
    {'name': 'pattern/group 10/0902.jpg', 'path': 'pattern/group 10/0902.jpg'},
    {'name': 'pattern/group 2/0202.jpg', 'path': 'pattern/group 2/0202.jpg'},
    {'name': 'pattern/group 6/0604.jpg', 'path': 'pattern/group 6/0604.jpg'},
    {'name': 'Stimuli/stimuli_1.jpeg', 'path': 'Stimuli/stimuli_1.jpeg'},
    {'name': 'pattern/group 9/0904.jpg', 'path': 'pattern/group 9/0904.jpg'},
    {'name': 'pattern/group 44/4403.jpg', 'path': 'pattern/group 44/4403.jpg'},
    {'name': 'pattern/group 16/1601.jpg', 'path': 'pattern/group 16/1601.jpg'},
    {'name': 'pattern/group 31/3101.jpg', 'path': 'pattern/group 31/3101.jpg'},
    {'name': 'pattern/group 28/2802.jpg', 'path': 'pattern/group 28/2802.jpg'},
    {'name': 'pattern/group 1/WeChat 圖片_20210605023530.jpg', 'path': 'pattern/group 1/WeChat 圖片_20210605023530.jpg'},
    {'name': 'pattern/group 16/1603.jpg', 'path': 'pattern/group 16/1603.jpg'},
    {'name': 'pattern/group 36/3603.jpg', 'path': 'pattern/group 36/3603.jpg'},
    {'name': 'pattern/group 47/4702.jpg', 'path': 'pattern/group 47/4702.jpg'},
    {'name': 'pattern/group 8/0802.jpg', 'path': 'pattern/group 8/0802.jpg'},
    {'name': 'pattern/group 47/4704.jpg', 'path': 'pattern/group 47/4704.jpg'},
    {'name': 'pattern/group 27/2702.jpg', 'path': 'pattern/group 27/2702.jpg'},
    {'name': 'pattern/group 14/1404.jpg', 'path': 'pattern/group 14/1404.jpg'},
    {'name': 'pattern/group 24/2402.jpg', 'path': 'pattern/group 24/2402.jpg'},
    {'name': 'pattern/group 35/3501.jpg', 'path': 'pattern/group 35/3501.jpg'},
    {'name': 'pattern/group 30/3001.jpg', 'path': 'pattern/group 30/3001.jpg'},
    {'name': 'pattern/group 39/3904.jpg', 'path': 'pattern/group 39/3904.jpg'},
    {'name': 'pattern/group 48/4801.jpg', 'path': 'pattern/group 48/4801.jpg'},
    {'name': 'pattern/group 33/3302.jpg', 'path': 'pattern/group 33/3302.jpg'},
    {'name': 'pattern/group 22/2201.jpg', 'path': 'pattern/group 22/2201.jpg'},
    {'name': 'pattern/group 2/0203.jpg', 'path': 'pattern/group 2/0203.jpg'},
    {'name': 'pattern/group 21/2103.jpg', 'path': 'pattern/group 21/2103.jpg'},
    {'name': 'pattern/group 29/2901.jpg', 'path': 'pattern/group 29/2901.jpg'},
    {'name': 'pattern/group 5/0502.jpg', 'path': 'pattern/group 5/0502.jpg'},
    {'name': 'pattern/group 18/1802.jpg', 'path': 'pattern/group 18/1802.jpg'},
    {'name': 'pattern/group 45/4502.jpg', 'path': 'pattern/group 45/4502.jpg'},
    {'name': 'pattern/group 37/3702.jpg', 'path': 'pattern/group 37/3702.jpg'},
    {'name': 'pattern/group 49/4901.jpg', 'path': 'pattern/group 49/4901.jpg'},
    {'name': 'pattern/group 28/2801.jpg', 'path': 'pattern/group 28/2801.jpg'},
    {'name': 'pattern/group 10/0904.jpg', 'path': 'pattern/group 10/0904.jpg'},
    {'name': 'image_stimuli.xlsx', 'path': 'image_stimuli.xlsx'},
    {'name': 'pattern/group 13/1304.jpg', 'path': 'pattern/group 13/1304.jpg'},
    {'name': 'pattern/group 25/2502.jpg', 'path': 'pattern/group 25/2502.jpg'},
    {'name': 'pattern/group 50/5001.jpg', 'path': 'pattern/group 50/5001.jpg'},
    {'name': 'pattern/group 13/1303.jpg', 'path': 'pattern/group 13/1303.jpg'},
    {'name': 'pattern/group 49/4904.jpg', 'path': 'pattern/group 49/4904.jpg'},
    {'name': 'Stimuli/stimuli_7.jpeg', 'path': 'Stimuli/stimuli_7.jpeg'},
    {'name': 'pattern/group 21/2102.jpg', 'path': 'pattern/group 21/2102.jpg'},
    {'name': 'pattern/group 9/0902.jpg', 'path': 'pattern/group 9/0902.jpg'},
    {'name': 'pattern/group 45/4503.jpg', 'path': 'pattern/group 45/4503.jpg'},
    {'name': 'Stimuli/stimuli_4.jpeg', 'path': 'Stimuli/stimuli_4.jpeg'},
    {'name': 'pattern/group 28/2803.jpg', 'path': 'pattern/group 28/2803.jpg'},
    {'name': 'pattern/group 50/5002.jpg', 'path': 'pattern/group 50/5002.jpg'},
    {'name': 'pattern/group 17/1701.jpg', 'path': 'pattern/group 17/1701.jpg'},
    {'name': 'pattern/group 20/2003.jpg', 'path': 'pattern/group 20/2003.jpg'},
    {'name': 'pattern/group 40/4001.jpg', 'path': 'pattern/group 40/4001.jpg'},
    {'name': 'pattern/group 44/4402.jpg', 'path': 'pattern/group 44/4402.jpg'},
    {'name': 'pattern/group 24/2404.jpg', 'path': 'pattern/group 24/2404.jpg'},
    {'name': 'pattern/group 12/1204.jpg', 'path': 'pattern/group 12/1204.jpg'},
    {'name': 'pattern/group 24/2401.jpg', 'path': 'pattern/group 24/2401.jpg'},
    {'name': 'Stimuli/stimuli_8.jpeg', 'path': 'Stimuli/stimuli_8.jpeg'},
    {'name': 'pattern/group 41/4104.jpg', 'path': 'pattern/group 41/4104.jpg'},
    {'name': 'pattern/group 23/2304.jpg', 'path': 'pattern/group 23/2304.jpg'},
    {'name': 'pattern/group 14/1402.jpg', 'path': 'pattern/group 14/1402.jpg'},
    {'name': 'pattern/group 36/3601.jpg', 'path': 'pattern/group 36/3601.jpg'},
    {'name': 'pattern/group 41/4102.jpg', 'path': 'pattern/group 41/4102.jpg'},
    {'name': 'pattern/group 25/2504.jpg', 'path': 'pattern/group 25/2504.jpg'},
    {'name': 'pattern/group 42/4202.jpg', 'path': 'pattern/group 42/4202.jpg'},
    {'name': 'pattern/group 18/1801.jpg', 'path': 'pattern/group 18/1801.jpg'},
    {'name': 'pattern/group 20/2002.jpg', 'path': 'pattern/group 20/2002.jpg'},
    {'name': 'pattern/group 17/1703.jpg', 'path': 'pattern/group 17/1703.jpg'},
    {'name': 'pattern/group 20/2001.jpg', 'path': 'pattern/group 20/2001.jpg'},
    {'name': 'pattern/group 29/2904.jpg', 'path': 'pattern/group 29/2904.jpg'},
    {'name': 'pattern/group 39/3902.jpg', 'path': 'pattern/group 39/3902.jpg'},
    {'name': 'pattern/group 48/4804.jpg', 'path': 'pattern/group 48/4804.jpg'},
    {'name': 'pattern/group 19/1902.jpg', 'path': 'pattern/group 19/1902.jpg'},
    {'name': 'pattern/group 3/0304.jpg', 'path': 'pattern/group 3/0304.jpg'},
    {'name': 'pattern/group 2/0204.jpg', 'path': 'pattern/group 2/0204.jpg'},
    {'name': 'pattern/group 37/3704.jpg', 'path': 'pattern/group 37/3704.jpg'},
    {'name': 'pattern/group 11/1103.jpg', 'path': 'pattern/group 11/1103.jpg'},
    {'name': 'pattern/group 35/3503.jpg', 'path': 'pattern/group 35/3503.jpg'},
    {'name': 'pattern/group 43/4301.jpg', 'path': 'pattern/group 43/4301.jpg'},
    {'name': 'pattern/group 30/3002.jpg', 'path': 'pattern/group 30/3002.jpg'},
    {'name': 'pattern/group 23/2303.jpg', 'path': 'pattern/group 23/2303.jpg'},
    {'name': 'pattern/group 4/0401.jpg', 'path': 'pattern/group 4/0401.jpg'},
    {'name': 'pattern/group 3/0302.jpg', 'path': 'pattern/group 3/0302.jpg'},
    {'name': 'pattern/group 40/4004.jpg', 'path': 'pattern/group 40/4004.jpg'},
    {'name': 'pattern/group 43/4302.jpg', 'path': 'pattern/group 43/4302.jpg'},
    {'name': 'pattern/group 11/1102.jpg', 'path': 'pattern/group 11/1102.jpg'},
    {'name': 'pattern/group 5/0503.jpg', 'path': 'pattern/group 5/0503.jpg'},
    {'name': 'pattern/group 21/2101.jpg', 'path': 'pattern/group 21/2101.jpg'},
    {'name': 'pattern/group 22/2202.jpg', 'path': 'pattern/group 22/2202.jpg'},
    {'name': 'pattern/group 31/3103.jpg', 'path': 'pattern/group 31/3103.jpg'},
    {'name': 'pattern/group 31/3104.jpg', 'path': 'pattern/group 31/3104.jpg'},
    {'name': 'pattern/group 7/0702.jpg', 'path': 'pattern/group 7/0702.jpg'},
    {'name': 'pattern/group 33/3301.jpg', 'path': 'pattern/group 33/3301.jpg'},
    {'name': 'pattern/group 26/2601.jpg', 'path': 'pattern/group 26/2601.jpg'},
    {'name': 'pattern/group 30/3004.jpg', 'path': 'pattern/group 30/3004.jpg'},
    {'name': 'pattern/group 15/1502.jpg', 'path': 'pattern/group 15/1502.jpg'},
    {'name': 'pattern/group 3/0301.jpg', 'path': 'pattern/group 3/0301.jpg'},
    {'name': 'pattern/group 20/2004.jpg', 'path': 'pattern/group 20/2004.jpg'},
    {'name': 'pattern/group 1/0104.jpg', 'path': 'pattern/group 1/0104.jpg'},
    {'name': 'pattern/group 47/4701.jpg', 'path': 'pattern/group 47/4701.jpg'},
    {'name': 'pattern/group 46/4603.jpg', 'path': 'pattern/group 46/4603.jpg'},
    {'name': 'Stimuli/stimuli_10.jpeg', 'path': 'Stimuli/stimuli_10.jpeg'},
    {'name': 'pattern/group 19/1901.jpg', 'path': 'pattern/group 19/1901.jpg'},
    {'name': 'pattern/group 27/2701.jpg', 'path': 'pattern/group 27/2701.jpg'},
    {'name': 'pattern/group 22/2203.jpg', 'path': 'pattern/group 22/2203.jpg'},
    {'name': 'pattern/group 29/2902.jpg', 'path': 'pattern/group 29/2902.jpg'},
    {'name': 'pattern/group 31/3102.jpg', 'path': 'pattern/group 31/3102.jpg'},
    {'name': 'pattern/group 38/3801.jpg', 'path': 'pattern/group 38/3801.jpg'},
    {'name': 'pattern/group 4/0404.jpg', 'path': 'pattern/group 4/0404.jpg'},
    {'name': 'pattern/group 9/0903.jpg', 'path': 'pattern/group 9/0903.jpg'},
    {'name': 'pattern/group 4/0402.jpg', 'path': 'pattern/group 4/0402.jpg'},
    {'name': 'pattern/group 6/0603.jpg', 'path': 'pattern/group 6/0603.jpg'},
    {'name': 'pattern/group 7/0701.jpg', 'path': 'pattern/group 7/0701.jpg'},
    {'name': 'pattern/group 7/0704.jpg', 'path': 'pattern/group 7/0704.jpg'},
    {'name': 'pattern/group 14/1403.jpg', 'path': 'pattern/group 14/1403.jpg'},
    {'name': 'pattern/group 18/1803.jpg', 'path': 'pattern/group 18/1803.jpg'},
    {'name': 'pattern/group 32/3203.jpg', 'path': 'pattern/group 32/3203.jpg'},
    {'name': 'pattern/group 33/3304.jpg', 'path': 'pattern/group 33/3304.jpg'},
    {'name': 'pattern/group 19/1903.jpg', 'path': 'pattern/group 19/1903.jpg'},
    {'name': 'pattern/group 4/0403.jpg', 'path': 'pattern/group 4/0403.jpg'},
    {'name': 'pattern/group 33/3303.jpg', 'path': 'pattern/group 33/3303.jpg'},
    {'name': 'Stimuli/stimuli_12.jpeg', 'path': 'Stimuli/stimuli_12.jpeg'},
    {'name': 'pattern/group 8/0803.jpg', 'path': 'pattern/group 8/0803.jpg'},
    {'name': 'pattern/group 42/4201.jpg', 'path': 'pattern/group 42/4201.jpg'},
    {'name': 'pattern/group 1/WeChat 圖片_20210605023530 - 副本.jpg', 'path': 'pattern/group 1/WeChat 圖片_20210605023530 - 副本.jpg'},
    {'name': 'pattern/group 28/2804.jpg', 'path': 'pattern/group 28/2804.jpg'},
    {'name': 'pattern/group 36/3604.jpg', 'path': 'pattern/group 36/3604.jpg'},
    {'name': 'pattern/group 37/3703.jpg', 'path': 'pattern/group 37/3703.jpg'},
    {'name': 'Stimuli/stimuli_5.jpeg', 'path': 'Stimuli/stimuli_5.jpeg'},
    {'name': 'pattern/group 13/1302.jpg', 'path': 'pattern/group 13/1302.jpg'},
    {'name': 'pattern/group 21/2104.jpg', 'path': 'pattern/group 21/2104.jpg'},
    {'name': 'pattern/group 15/1504.jpg', 'path': 'pattern/group 15/1504.jpg'},
    {'name': 'pattern/group 47/4703.jpg', 'path': 'pattern/group 47/4703.jpg'},
    {'name': 'pattern/group 10/0903.jpg', 'path': 'pattern/group 10/0903.jpg'},
    {'name': 'pattern/group 6/0602.jpg', 'path': 'pattern/group 6/0602.jpg'},
    {'name': 'pattern/group 34/3402.jpg', 'path': 'pattern/group 34/3402.jpg'},
    {'name': 'pattern/group 43/4303.jpg', 'path': 'pattern/group 43/4303.jpg'},
    {'name': 'pattern/group 35/3504.jpg', 'path': 'pattern/group 35/3504.jpg'},
    {'name': 'pattern/group 12/1202.jpg', 'path': 'pattern/group 12/1202.jpg'},
    {'name': 'pattern/group 50/5003.jpg', 'path': 'pattern/group 50/5003.jpg'},
    {'name': 'pattern/group 17/1704.jpg', 'path': 'pattern/group 17/1704.jpg'},
    {'name': 'pattern/group 49/4903.jpg', 'path': 'pattern/group 49/4903.jpg'},
    {'name': 'pattern/group 13/1301.jpg', 'path': 'pattern/group 13/1301.jpg'},
    {'name': 'Stimuli/stimuli_11.jpeg', 'path': 'Stimuli/stimuli_11.jpeg'},
    {'name': 'Stimuli/stimuli_6.jpeg', 'path': 'Stimuli/stimuli_6.jpeg'},
    {'name': 'pattern/group 23/2301.jpg', 'path': 'pattern/group 23/2301.jpg'},
    {'name': 'pattern/group 48/4803.jpg', 'path': 'pattern/group 48/4803.jpg'},
    {'name': 'pattern/group 37/3701.jpg', 'path': 'pattern/group 37/3701.jpg'},
    {'name': 'Stimuli/stimuli_2.jpeg', 'path': 'Stimuli/stimuli_2.jpeg'},
    {'name': 'pattern/group 6/0601.jpg', 'path': 'pattern/group 6/0601.jpg'},
    {'name': 'pattern/group 25/2503.jpg', 'path': 'pattern/group 25/2503.jpg'},
    {'name': 'pattern/group 11/1104.jpg', 'path': 'pattern/group 11/1104.jpg'},
    {'name': 'pattern/group 9/0901.jpg', 'path': 'pattern/group 9/0901.jpg'},
    {'name': 'pattern/group 30/3003.jpg', 'path': 'pattern/group 30/3003.jpg'},
    {'name': 'pattern/group 26/2603.jpg', 'path': 'pattern/group 26/2603.jpg'},
    {'name': 'pattern/group 2/0201.jpg', 'path': 'pattern/group 2/0201.jpg'},
    {'name': 'pattern/group 42/4204.jpg', 'path': 'pattern/group 42/4204.jpg'},
    {'name': 'pattern/group 49/4902.jpg', 'path': 'pattern/group 49/4902.jpg'},
    {'name': 'Stimuli/stimuli_3.jpeg', 'path': 'Stimuli/stimuli_3.jpeg'},
    {'name': 'pattern/group 15/1503.jpg', 'path': 'pattern/group 15/1503.jpg'},
    {'name': 'pattern/group 34/3403.jpg', 'path': 'pattern/group 34/3403.jpg'},
    {'name': 'pattern/group 38/3802.jpg', 'path': 'pattern/group 38/3802.jpg'},
    {'name': 'pattern/group 10/0901.jpg', 'path': 'pattern/group 10/0901.jpg'},
    {'name': 'pattern/group 8/0804.jpg', 'path': 'pattern/group 8/0804.jpg'},
    {'name': 'pattern/group 27/2704.jpg', 'path': 'pattern/group 27/2704.jpg'}
  ]
});

psychoJS.experimentLogger.setLevel(core.Logger.ServerLevel.EXP);


var frameDur;
function updateInfo() {
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2021.1.4';
  expInfo['OS'] = window.navigator.platform;

  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  
  return Scheduler.Event.NEXT;
}


var ConsentClock;
var textConsent;
var keyconsent;
var WelcomeClock;
var textWelcome;
var keywelcome;
var InstructionClock;
var textintroduction;
var keyintroduction;
var trialClock;
var image;
var key_resp;
var imageT1;
var imageT2;
var imageT3;
var imageT4;
var text_2;
var text_3;
var text_4;
var text_5;
var Interruption1Clock;
var text;
var Nextsession;
var EndAndDebriefClock;
var textThankYou;
var globalClock;
var routineTimer;
function experimentInit() {
  // Initialize components for Routine "Consent"
  ConsentClock = new util.Clock();
  textConsent = new visual.TextStim({
    win: psychoJS.window,
    name: 'textConsent',
    text: 'Please make sure you have read the consent form and agree to particiate before you click any keys.\n\nParticipation is completely voluntary.\n\nPress space to continue.',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.075,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  keyconsent = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "Welcome"
  WelcomeClock = new util.Clock();
  textWelcome = new visual.TextStim({
    win: psychoJS.window,
    name: 'textWelcome',
    text: 'Welcome to the visual short-term memory experiment! \n\nThank you so much to participate!\n\nPress space to continue.',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.075,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  keywelcome = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "Instruction"
  InstructionClock = new util.Clock();
  textintroduction = new visual.TextStim({
    win: psychoJS.window,
    name: 'textintroduction',
    text: 'You will be shown one photos for a short while, afterwards, you will be shown four choices.\n\nChose the one you think you have seen.\n\nPress space to enter the training phase.',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.075,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  keyintroduction = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "trial"
  trialClock = new util.Clock();
  image = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0, 0], size : [0.5, 0.5],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  imageT1 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'imageT1', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [(- 0.375), 0], size : [0.25, 0.25],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -2.0 
  });
  imageT2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'imageT2', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [(- 0.125), 0], size : [0.25, 0.25],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -3.0 
  });
  imageT3 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'imageT3', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0.125, 0], size : [0.25, 0.25],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -4.0 
  });
  imageT4 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'imageT4', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0.375, 0], size : [0.25, 0.25],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -5.0 
  });
  text_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_2',
    text: '1',
    font: 'Open Sans',
    units: undefined, 
    pos: [(- 0.375), (- 0.25)], height: 0.1,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: -6.0 
  });
  
  text_3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_3',
    text: '2',
    font: 'Open Sans',
    units: undefined, 
    pos: [(- 0.125), (- 0.25)], height: 0.1,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: -7.0 
  });
  
  text_4 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_4',
    text: '3',
    font: 'Open Sans',
    units: undefined, 
    pos: [0.125, (- 0.25)], height: 0.1,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: -8.0 
  });
  
  text_5 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_5',
    text: '4',
    font: 'Open Sans',
    units: undefined, 
    pos: [0.375, (- 0.25)], height: 0.1,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: -9.0 
  });
  
  // Initialize components for Routine "Interruption1"
  Interruption1Clock = new util.Clock();
  text = new visual.TextStim({
    win: psychoJS.window,
    name: 'text',
    text: 'Wait for instruction from the monitor.\n\nPress space only when told to do so.\n\nThank you!',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.075,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  Nextsession = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "trial"
  trialClock = new util.Clock();
  image = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0, 0], size : [0.5, 0.5],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  imageT1 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'imageT1', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [(- 0.375), 0], size : [0.25, 0.25],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -2.0 
  });
  imageT2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'imageT2', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [(- 0.125), 0], size : [0.25, 0.25],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -3.0 
  });
  imageT3 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'imageT3', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0.125, 0], size : [0.25, 0.25],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -4.0 
  });
  imageT4 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'imageT4', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0.375, 0], size : [0.25, 0.25],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -5.0 
  });
  text_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_2',
    text: '1',
    font: 'Open Sans',
    units: undefined, 
    pos: [(- 0.375), (- 0.25)], height: 0.1,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: -6.0 
  });
  
  text_3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_3',
    text: '2',
    font: 'Open Sans',
    units: undefined, 
    pos: [(- 0.125), (- 0.25)], height: 0.1,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: -7.0 
  });
  
  text_4 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_4',
    text: '3',
    font: 'Open Sans',
    units: undefined, 
    pos: [0.125, (- 0.25)], height: 0.1,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: -8.0 
  });
  
  text_5 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_5',
    text: '4',
    font: 'Open Sans',
    units: undefined, 
    pos: [0.375, (- 0.25)], height: 0.1,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: -9.0 
  });
  
  // Initialize components for Routine "Interruption1"
  Interruption1Clock = new util.Clock();
  text = new visual.TextStim({
    win: psychoJS.window,
    name: 'text',
    text: 'Wait for instruction from the monitor.\n\nPress space only when told to do so.\n\nThank you!',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.075,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  Nextsession = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "trial"
  trialClock = new util.Clock();
  image = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0, 0], size : [0.5, 0.5],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  imageT1 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'imageT1', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [(- 0.375), 0], size : [0.25, 0.25],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -2.0 
  });
  imageT2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'imageT2', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [(- 0.125), 0], size : [0.25, 0.25],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -3.0 
  });
  imageT3 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'imageT3', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0.125, 0], size : [0.25, 0.25],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -4.0 
  });
  imageT4 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'imageT4', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0.375, 0], size : [0.25, 0.25],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -5.0 
  });
  text_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_2',
    text: '1',
    font: 'Open Sans',
    units: undefined, 
    pos: [(- 0.375), (- 0.25)], height: 0.1,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: -6.0 
  });
  
  text_3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_3',
    text: '2',
    font: 'Open Sans',
    units: undefined, 
    pos: [(- 0.125), (- 0.25)], height: 0.1,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: -7.0 
  });
  
  text_4 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_4',
    text: '3',
    font: 'Open Sans',
    units: undefined, 
    pos: [0.125, (- 0.25)], height: 0.1,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: -8.0 
  });
  
  text_5 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_5',
    text: '4',
    font: 'Open Sans',
    units: undefined, 
    pos: [0.375, (- 0.25)], height: 0.1,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: -9.0 
  });
  
  // Initialize components for Routine "Interruption1"
  Interruption1Clock = new util.Clock();
  text = new visual.TextStim({
    win: psychoJS.window,
    name: 'text',
    text: 'Wait for instruction from the monitor.\n\nPress space only when told to do so.\n\nThank you!',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.075,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  Nextsession = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "trial"
  trialClock = new util.Clock();
  image = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0, 0], size : [0.5, 0.5],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  imageT1 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'imageT1', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [(- 0.375), 0], size : [0.25, 0.25],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -2.0 
  });
  imageT2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'imageT2', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [(- 0.125), 0], size : [0.25, 0.25],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -3.0 
  });
  imageT3 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'imageT3', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0.125, 0], size : [0.25, 0.25],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -4.0 
  });
  imageT4 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'imageT4', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0.375, 0], size : [0.25, 0.25],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -5.0 
  });
  text_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_2',
    text: '1',
    font: 'Open Sans',
    units: undefined, 
    pos: [(- 0.375), (- 0.25)], height: 0.1,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: -6.0 
  });
  
  text_3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_3',
    text: '2',
    font: 'Open Sans',
    units: undefined, 
    pos: [(- 0.125), (- 0.25)], height: 0.1,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: -7.0 
  });
  
  text_4 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_4',
    text: '3',
    font: 'Open Sans',
    units: undefined, 
    pos: [0.125, (- 0.25)], height: 0.1,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: -8.0 
  });
  
  text_5 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_5',
    text: '4',
    font: 'Open Sans',
    units: undefined, 
    pos: [0.375, (- 0.25)], height: 0.1,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: -9.0 
  });
  
  // Initialize components for Routine "Interruption1"
  Interruption1Clock = new util.Clock();
  text = new visual.TextStim({
    win: psychoJS.window,
    name: 'text',
    text: 'Wait for instruction from the monitor.\n\nPress space only when told to do so.\n\nThank you!',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.075,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  Nextsession = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "trial"
  trialClock = new util.Clock();
  image = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0, 0], size : [0.5, 0.5],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  imageT1 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'imageT1', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [(- 0.375), 0], size : [0.25, 0.25],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -2.0 
  });
  imageT2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'imageT2', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [(- 0.125), 0], size : [0.25, 0.25],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -3.0 
  });
  imageT3 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'imageT3', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0.125, 0], size : [0.25, 0.25],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -4.0 
  });
  imageT4 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'imageT4', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0.375, 0], size : [0.25, 0.25],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -5.0 
  });
  text_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_2',
    text: '1',
    font: 'Open Sans',
    units: undefined, 
    pos: [(- 0.375), (- 0.25)], height: 0.1,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: -6.0 
  });
  
  text_3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_3',
    text: '2',
    font: 'Open Sans',
    units: undefined, 
    pos: [(- 0.125), (- 0.25)], height: 0.1,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: -7.0 
  });
  
  text_4 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_4',
    text: '3',
    font: 'Open Sans',
    units: undefined, 
    pos: [0.125, (- 0.25)], height: 0.1,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: -8.0 
  });
  
  text_5 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_5',
    text: '4',
    font: 'Open Sans',
    units: undefined, 
    pos: [0.375, (- 0.25)], height: 0.1,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: -9.0 
  });
  
  // Initialize components for Routine "Interruption1"
  Interruption1Clock = new util.Clock();
  text = new visual.TextStim({
    win: psychoJS.window,
    name: 'text',
    text: 'Wait for instruction from the monitor.\n\nPress space only when told to do so.\n\nThank you!',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.075,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  Nextsession = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "trial"
  trialClock = new util.Clock();
  image = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0, 0], size : [0.5, 0.5],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  imageT1 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'imageT1', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [(- 0.375), 0], size : [0.25, 0.25],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -2.0 
  });
  imageT2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'imageT2', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [(- 0.125), 0], size : [0.25, 0.25],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -3.0 
  });
  imageT3 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'imageT3', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0.125, 0], size : [0.25, 0.25],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -4.0 
  });
  imageT4 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'imageT4', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0.375, 0], size : [0.25, 0.25],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -5.0 
  });
  text_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_2',
    text: '1',
    font: 'Open Sans',
    units: undefined, 
    pos: [(- 0.375), (- 0.25)], height: 0.1,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: -6.0 
  });
  
  text_3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_3',
    text: '2',
    font: 'Open Sans',
    units: undefined, 
    pos: [(- 0.125), (- 0.25)], height: 0.1,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: -7.0 
  });
  
  text_4 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_4',
    text: '3',
    font: 'Open Sans',
    units: undefined, 
    pos: [0.125, (- 0.25)], height: 0.1,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: -8.0 
  });
  
  text_5 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_5',
    text: '4',
    font: 'Open Sans',
    units: undefined, 
    pos: [0.375, (- 0.25)], height: 0.1,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: -9.0 
  });
  
  // Initialize components for Routine "EndAndDebrief"
  EndAndDebriefClock = new util.Clock();
  textThankYou = new visual.TextStim({
    win: psychoJS.window,
    name: 'textThankYou',
    text: 'Thank you for your participation.\n\nPlease reach out to the monitor if you would like a debrief.\n\nPress esc to exit only when told to do so.',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.075,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}


var t;
var frameN;
var continueRoutine;
var _keyconsent_allKeys;
var ConsentComponents;
function ConsentRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'Consent'-------
    t = 0;
    ConsentClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    keyconsent.keys = undefined;
    keyconsent.rt = undefined;
    _keyconsent_allKeys = [];
    // keep track of which components have finished
    ConsentComponents = [];
    ConsentComponents.push(textConsent);
    ConsentComponents.push(keyconsent);
    
    for (const thisComponent of ConsentComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function ConsentRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'Consent'-------
    // get current time
    t = ConsentClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *textConsent* updates
    if (t >= 0.0 && textConsent.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      textConsent.tStart = t;  // (not accounting for frame time here)
      textConsent.frameNStart = frameN;  // exact frame index
      
      textConsent.setAutoDraw(true);
    }

    
    // *keyconsent* updates
    if (t >= 0.0 && keyconsent.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      keyconsent.tStart = t;  // (not accounting for frame time here)
      keyconsent.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { keyconsent.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { keyconsent.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { keyconsent.clearEvents(); });
    }

    if (keyconsent.status === PsychoJS.Status.STARTED) {
      let theseKeys = keyconsent.getKeys({keyList: ['space'], waitRelease: false});
      _keyconsent_allKeys = _keyconsent_allKeys.concat(theseKeys);
      if (_keyconsent_allKeys.length > 0) {
        keyconsent.keys = _keyconsent_allKeys[_keyconsent_allKeys.length - 1].name;  // just the last key pressed
        keyconsent.rt = _keyconsent_allKeys[_keyconsent_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of ConsentComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function ConsentRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'Consent'-------
    for (const thisComponent of ConsentComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('keyconsent.keys', keyconsent.keys);
    if (typeof keyconsent.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('keyconsent.rt', keyconsent.rt);
        routineTimer.reset();
        }
    
    keyconsent.stop();
    // the Routine "Consent" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _keywelcome_allKeys;
var WelcomeComponents;
function WelcomeRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'Welcome'-------
    t = 0;
    WelcomeClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    keywelcome.keys = undefined;
    keywelcome.rt = undefined;
    _keywelcome_allKeys = [];
    // keep track of which components have finished
    WelcomeComponents = [];
    WelcomeComponents.push(textWelcome);
    WelcomeComponents.push(keywelcome);
    
    for (const thisComponent of WelcomeComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function WelcomeRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'Welcome'-------
    // get current time
    t = WelcomeClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *textWelcome* updates
    if (t >= 0.0 && textWelcome.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      textWelcome.tStart = t;  // (not accounting for frame time here)
      textWelcome.frameNStart = frameN;  // exact frame index
      
      textWelcome.setAutoDraw(true);
    }

    
    // *keywelcome* updates
    if (t >= 0.0 && keywelcome.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      keywelcome.tStart = t;  // (not accounting for frame time here)
      keywelcome.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { keywelcome.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { keywelcome.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { keywelcome.clearEvents(); });
    }

    if (keywelcome.status === PsychoJS.Status.STARTED) {
      let theseKeys = keywelcome.getKeys({keyList: ['space'], waitRelease: false});
      _keywelcome_allKeys = _keywelcome_allKeys.concat(theseKeys);
      if (_keywelcome_allKeys.length > 0) {
        keywelcome.keys = _keywelcome_allKeys[_keywelcome_allKeys.length - 1].name;  // just the last key pressed
        keywelcome.rt = _keywelcome_allKeys[_keywelcome_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of WelcomeComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function WelcomeRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'Welcome'-------
    for (const thisComponent of WelcomeComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('keywelcome.keys', keywelcome.keys);
    if (typeof keywelcome.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('keywelcome.rt', keywelcome.rt);
        routineTimer.reset();
        }
    
    keywelcome.stop();
    // the Routine "Welcome" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _keyintroduction_allKeys;
var InstructionComponents;
function InstructionRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'Instruction'-------
    t = 0;
    InstructionClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    keyintroduction.keys = undefined;
    keyintroduction.rt = undefined;
    _keyintroduction_allKeys = [];
    // keep track of which components have finished
    InstructionComponents = [];
    InstructionComponents.push(textintroduction);
    InstructionComponents.push(keyintroduction);
    
    for (const thisComponent of InstructionComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function InstructionRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'Instruction'-------
    // get current time
    t = InstructionClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *textintroduction* updates
    if (t >= 0.0 && textintroduction.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      textintroduction.tStart = t;  // (not accounting for frame time here)
      textintroduction.frameNStart = frameN;  // exact frame index
      
      textintroduction.setAutoDraw(true);
    }

    
    // *keyintroduction* updates
    if (t >= 0.0 && keyintroduction.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      keyintroduction.tStart = t;  // (not accounting for frame time here)
      keyintroduction.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { keyintroduction.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { keyintroduction.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { keyintroduction.clearEvents(); });
    }

    if (keyintroduction.status === PsychoJS.Status.STARTED) {
      let theseKeys = keyintroduction.getKeys({keyList: ['space'], waitRelease: false});
      _keyintroduction_allKeys = _keyintroduction_allKeys.concat(theseKeys);
      if (_keyintroduction_allKeys.length > 0) {
        keyintroduction.keys = _keyintroduction_allKeys[_keyintroduction_allKeys.length - 1].name;  // just the last key pressed
        keyintroduction.rt = _keyintroduction_allKeys[_keyintroduction_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of InstructionComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function InstructionRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'Instruction'-------
    for (const thisComponent of InstructionComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('keyintroduction.keys', keyintroduction.keys);
    if (typeof keyintroduction.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('keyintroduction.rt', keyintroduction.rt);
        routineTimer.reset();
        }
    
    keyintroduction.stop();
    // the Routine "Instruction" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var trials_7;
var currentLoop;
function trials_7LoopBegin(trials_7LoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  trials_7 = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 2, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: TrialHandler.importConditions(psychoJS.serverManager, 'image_stimuli.xlsx', '51:53'),
    seed: undefined, name: 'trials_7'
  });
  psychoJS.experiment.addLoop(trials_7); // add the loop to the experiment
  currentLoop = trials_7;  // we're now the current loop

  // Schedule all the trials in the trialList:
  for (const thisTrial_7 of trials_7) {
    const snapshot = trials_7.getSnapshot();
    trials_7LoopScheduler.add(importConditions(snapshot));
    trials_7LoopScheduler.add(trialRoutineBegin(snapshot));
    trials_7LoopScheduler.add(trialRoutineEachFrame(snapshot));
    trials_7LoopScheduler.add(trialRoutineEnd(snapshot));
    trials_7LoopScheduler.add(endLoopIteration(trials_7LoopScheduler, snapshot));
  }

  return Scheduler.Event.NEXT;
}


function trials_7LoopEnd() {
  psychoJS.experiment.removeLoop(trials_7);

  return Scheduler.Event.NEXT;
}


var trials;
function trialsLoopBegin(trialsLoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  trials = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: TrialHandler.importConditions(psychoJS.serverManager, '/Users/athenahuang/Downloads/CIS Experiment/image_stimuli.xlsx', '0:10'),
    seed: undefined, name: 'trials'
  });
  psychoJS.experiment.addLoop(trials); // add the loop to the experiment
  currentLoop = trials;  // we're now the current loop

  // Schedule all the trials in the trialList:
  for (const thisTrial of trials) {
    const snapshot = trials.getSnapshot();
    trialsLoopScheduler.add(importConditions(snapshot));
    trialsLoopScheduler.add(trialRoutineBegin(snapshot));
    trialsLoopScheduler.add(trialRoutineEachFrame(snapshot));
    trialsLoopScheduler.add(trialRoutineEnd(snapshot));
    trialsLoopScheduler.add(endLoopIteration(trialsLoopScheduler, snapshot));
  }

  return Scheduler.Event.NEXT;
}


function trialsLoopEnd() {
  psychoJS.experiment.removeLoop(trials);

  return Scheduler.Event.NEXT;
}


var trials_2;
function trials_2LoopBegin(trials_2LoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  trials_2 = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: TrialHandler.importConditions(psychoJS.serverManager, 'image_stimuli.xlsx', '10:20'),
    seed: undefined, name: 'trials_2'
  });
  psychoJS.experiment.addLoop(trials_2); // add the loop to the experiment
  currentLoop = trials_2;  // we're now the current loop

  // Schedule all the trials in the trialList:
  for (const thisTrial_2 of trials_2) {
    const snapshot = trials_2.getSnapshot();
    trials_2LoopScheduler.add(importConditions(snapshot));
    trials_2LoopScheduler.add(trialRoutineBegin(snapshot));
    trials_2LoopScheduler.add(trialRoutineEachFrame(snapshot));
    trials_2LoopScheduler.add(trialRoutineEnd(snapshot));
    trials_2LoopScheduler.add(endLoopIteration(trials_2LoopScheduler, snapshot));
  }

  return Scheduler.Event.NEXT;
}


function trials_2LoopEnd() {
  psychoJS.experiment.removeLoop(trials_2);

  return Scheduler.Event.NEXT;
}


var trials_3;
function trials_3LoopBegin(trials_3LoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  trials_3 = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: TrialHandler.importConditions(psychoJS.serverManager, 'image_stimuli.xlsx', '20:30'),
    seed: undefined, name: 'trials_3'
  });
  psychoJS.experiment.addLoop(trials_3); // add the loop to the experiment
  currentLoop = trials_3;  // we're now the current loop

  // Schedule all the trials in the trialList:
  for (const thisTrial_3 of trials_3) {
    const snapshot = trials_3.getSnapshot();
    trials_3LoopScheduler.add(importConditions(snapshot));
    trials_3LoopScheduler.add(trialRoutineBegin(snapshot));
    trials_3LoopScheduler.add(trialRoutineEachFrame(snapshot));
    trials_3LoopScheduler.add(trialRoutineEnd(snapshot));
    trials_3LoopScheduler.add(endLoopIteration(trials_3LoopScheduler, snapshot));
  }

  return Scheduler.Event.NEXT;
}


function trials_3LoopEnd() {
  psychoJS.experiment.removeLoop(trials_3);

  return Scheduler.Event.NEXT;
}


var trials_4;
function trials_4LoopBegin(trials_4LoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  trials_4 = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: TrialHandler.importConditions(psychoJS.serverManager, 'image_stimuli.xlsx', '30:40'),
    seed: undefined, name: 'trials_4'
  });
  psychoJS.experiment.addLoop(trials_4); // add the loop to the experiment
  currentLoop = trials_4;  // we're now the current loop

  // Schedule all the trials in the trialList:
  for (const thisTrial_4 of trials_4) {
    const snapshot = trials_4.getSnapshot();
    trials_4LoopScheduler.add(importConditions(snapshot));
    trials_4LoopScheduler.add(trialRoutineBegin(snapshot));
    trials_4LoopScheduler.add(trialRoutineEachFrame(snapshot));
    trials_4LoopScheduler.add(trialRoutineEnd(snapshot));
    trials_4LoopScheduler.add(endLoopIteration(trials_4LoopScheduler, snapshot));
  }

  return Scheduler.Event.NEXT;
}


function trials_4LoopEnd() {
  psychoJS.experiment.removeLoop(trials_4);

  return Scheduler.Event.NEXT;
}


var trials_5;
function trials_5LoopBegin(trials_5LoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  trials_5 = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: TrialHandler.importConditions(psychoJS.serverManager, 'image_stimuli.xlsx', '40:50'),
    seed: undefined, name: 'trials_5'
  });
  psychoJS.experiment.addLoop(trials_5); // add the loop to the experiment
  currentLoop = trials_5;  // we're now the current loop

  // Schedule all the trials in the trialList:
  for (const thisTrial_5 of trials_5) {
    const snapshot = trials_5.getSnapshot();
    trials_5LoopScheduler.add(importConditions(snapshot));
    trials_5LoopScheduler.add(trialRoutineBegin(snapshot));
    trials_5LoopScheduler.add(trialRoutineEachFrame(snapshot));
    trials_5LoopScheduler.add(trialRoutineEnd(snapshot));
    trials_5LoopScheduler.add(endLoopIteration(trials_5LoopScheduler, snapshot));
  }

  return Scheduler.Event.NEXT;
}


function trials_5LoopEnd() {
  psychoJS.experiment.removeLoop(trials_5);

  return Scheduler.Event.NEXT;
}


var _key_resp_allKeys;
var trialComponents;
function trialRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'trial'-------
    t = 0;
    trialClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    image.setImage(ImageFile);
    key_resp.keys = undefined;
    key_resp.rt = undefined;
    _key_resp_allKeys = [];
    imageT1.setImage(ImageFile1);
    imageT2.setImage(ImageFile2);
    imageT3.setImage(ImageFile3);
    imageT4.setImage(ImageFile4);
    // keep track of which components have finished
    trialComponents = [];
    trialComponents.push(image);
    trialComponents.push(key_resp);
    trialComponents.push(imageT1);
    trialComponents.push(imageT2);
    trialComponents.push(imageT3);
    trialComponents.push(imageT4);
    trialComponents.push(text_2);
    trialComponents.push(text_3);
    trialComponents.push(text_4);
    trialComponents.push(text_5);
    
    for (const thisComponent of trialComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


var frameRemains;
function trialRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'trial'-------
    // get current time
    t = trialClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *image* updates
    if (t >= 0.0 && image.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image.tStart = t;  // (not accounting for frame time here)
      image.frameNStart = frameN;  // exact frame index
      
      image.setAutoDraw(true);
    }

    frameRemains = 0.0 + 0.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (image.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      image.setAutoDraw(false);
    }
    
    // *key_resp* updates
    if (t >= 5.5 && key_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp.tStart = t;  // (not accounting for frame time here)
      key_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp.clearEvents(); });
    }

    if (key_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp.getKeys({keyList: ['1', '2', '3', '4'], waitRelease: false});
      _key_resp_allKeys = _key_resp_allKeys.concat(theseKeys);
      if (_key_resp_allKeys.length > 0) {
        key_resp.keys = _key_resp_allKeys[_key_resp_allKeys.length - 1].name;  // just the last key pressed
        key_resp.rt = _key_resp_allKeys[_key_resp_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *imageT1* updates
    if (t >= 5.5 && imageT1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      imageT1.tStart = t;  // (not accounting for frame time here)
      imageT1.frameNStart = frameN;  // exact frame index
      
      imageT1.setAutoDraw(true);
    }

    
    // *imageT2* updates
    if (t >= 5.5 && imageT2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      imageT2.tStart = t;  // (not accounting for frame time here)
      imageT2.frameNStart = frameN;  // exact frame index
      
      imageT2.setAutoDraw(true);
    }

    
    // *imageT3* updates
    if (t >= 5.5 && imageT3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      imageT3.tStart = t;  // (not accounting for frame time here)
      imageT3.frameNStart = frameN;  // exact frame index
      
      imageT3.setAutoDraw(true);
    }

    
    // *imageT4* updates
    if (t >= 5.5 && imageT4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      imageT4.tStart = t;  // (not accounting for frame time here)
      imageT4.frameNStart = frameN;  // exact frame index
      
      imageT4.setAutoDraw(true);
    }

    
    // *text_2* updates
    if (t >= 5.5 && text_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_2.tStart = t;  // (not accounting for frame time here)
      text_2.frameNStart = frameN;  // exact frame index
      
      text_2.setAutoDraw(true);
    }

    
    // *text_3* updates
    if (t >= 5.5 && text_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_3.tStart = t;  // (not accounting for frame time here)
      text_3.frameNStart = frameN;  // exact frame index
      
      text_3.setAutoDraw(true);
    }

    
    // *text_4* updates
    if (t >= 5.5 && text_4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_4.tStart = t;  // (not accounting for frame time here)
      text_4.frameNStart = frameN;  // exact frame index
      
      text_4.setAutoDraw(true);
    }

    
    // *text_5* updates
    if (t >= 5.5 && text_5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_5.tStart = t;  // (not accounting for frame time here)
      text_5.frameNStart = frameN;  // exact frame index
      
      text_5.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of trialComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function trialRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'trial'-------
    for (const thisComponent of trialComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('key_resp.keys', key_resp.keys);
    if (typeof key_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp.rt', key_resp.rt);
        routineTimer.reset();
        }
    
    key_resp.stop();
    // the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _Nextsession_allKeys;
var Interruption1Components;
function Interruption1RoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'Interruption1'-------
    t = 0;
    Interruption1Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    Nextsession.keys = undefined;
    Nextsession.rt = undefined;
    _Nextsession_allKeys = [];
    // keep track of which components have finished
    Interruption1Components = [];
    Interruption1Components.push(text);
    Interruption1Components.push(Nextsession);
    
    for (const thisComponent of Interruption1Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function Interruption1RoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'Interruption1'-------
    // get current time
    t = Interruption1Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text* updates
    if (t >= 0.0 && text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text.tStart = t;  // (not accounting for frame time here)
      text.frameNStart = frameN;  // exact frame index
      
      text.setAutoDraw(true);
    }

    
    // *Nextsession* updates
    if (t >= 0.0 && Nextsession.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Nextsession.tStart = t;  // (not accounting for frame time here)
      Nextsession.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { Nextsession.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { Nextsession.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { Nextsession.clearEvents(); });
    }

    if (Nextsession.status === PsychoJS.Status.STARTED) {
      let theseKeys = Nextsession.getKeys({keyList: ['space'], waitRelease: false});
      _Nextsession_allKeys = _Nextsession_allKeys.concat(theseKeys);
      if (_Nextsession_allKeys.length > 0) {
        Nextsession.keys = _Nextsession_allKeys[_Nextsession_allKeys.length - 1].name;  // just the last key pressed
        Nextsession.rt = _Nextsession_allKeys[_Nextsession_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of Interruption1Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function Interruption1RoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'Interruption1'-------
    for (const thisComponent of Interruption1Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('Nextsession.keys', Nextsession.keys);
    if (typeof Nextsession.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('Nextsession.rt', Nextsession.rt);
        routineTimer.reset();
        }
    
    Nextsession.stop();
    // the Routine "Interruption1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var EndAndDebriefComponents;
function EndAndDebriefRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'EndAndDebrief'-------
    t = 0;
    EndAndDebriefClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    // keep track of which components have finished
    EndAndDebriefComponents = [];
    EndAndDebriefComponents.push(textThankYou);
    
    for (const thisComponent of EndAndDebriefComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function EndAndDebriefRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'EndAndDebrief'-------
    // get current time
    t = EndAndDebriefClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *textThankYou* updates
    if (t >= 0.0 && textThankYou.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      textThankYou.tStart = t;  // (not accounting for frame time here)
      textThankYou.frameNStart = frameN;  // exact frame index
      
      textThankYou.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of EndAndDebriefComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function EndAndDebriefRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'EndAndDebrief'-------
    for (const thisComponent of EndAndDebriefComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // the Routine "EndAndDebrief" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


function endLoopIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        const thisTrial = snapshot.getCurrentTrial();
        if (typeof thisTrial === 'undefined' || !('isTrials' in thisTrial) || thisTrial.isTrials) {
          psychoJS.experiment.nextEntry(snapshot);
        }
      }
    return Scheduler.Event.NEXT;
    }
  };
}


function importConditions(currentLoop) {
  return function () {
    psychoJS.importAttributes(currentLoop.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}


function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (psychoJS.experiment.isEntryEmpty()) {
    psychoJS.experiment.nextEntry();
  }
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});
  
  return Scheduler.Event.QUIT;
}
