import cx_Oracle
import os, sys, io

def getConfigurationTable(run_num):
    print "\nDownloading ConfigurationTable for run {0}".format(run_num)

    db = cx_Oracle.connect('GEM_904_COND/904CondDB@INT2R')
    cur = db.cursor()

    query = "select * from CMS_GEM_MUON_VIEW.QC8_GEM_STAND_GEOMETRY_VIEW_RH where RUN_NUMBER="+str(run_num)
    cur.execute(query)

    configTablesPath = os.path.abspath("dumpDBtables.py").split('QC8Test')[0] + 'QC8Test/src/Analysis/GEMQC8/data/StandConfigurationTables/'
    outfile_name = configTablesPath + "StandGeometryConfiguration_run{0}.csv".format(run_num)

    with open(outfile_name,"w+") as outfile:
        line = "CH_SERIAL_NUMBER,GEM_NUM,POSITION,CH_TYPE,FLIP,AMC,OH,FLOW_METER,RUN_NUMBER\n"
        outfile.write(line)
        for result in cur:
            chamber_name = result[0]
            gem_num      = result[1]
            position     = result[2]
            ch_type      = result[3]
            flip         = result[4]
            amc          = result[5]
            oh           = result[6]
            flow_meter   = result[7]
            run_number   = result[8]
            line = str(chamber_name) + "," + str(gem_num) + "," + str(position) + "," + str(ch_type) + "," + str(flip) + "," + str(amc) + "," + str(oh) + "," + str(flow_meter) + "," + str(run_number) + "\n"
            outfile.write(line)

    print "\nSuccesfully done!\n"

def getAlignmentTable(run_num):
    print "\nDownloading AlignmentTable for run {0}".format(run_num)

    db = cx_Oracle.connect('GEM_904_COND/904CondDB@INT2R')
    cur = db.cursor()

    query = "select * from CMS_GEM_MUON_VIEW.QC8_GEM_ALIGNMENT_VIEW_RH where RUN_NUMBER="+str(run_num)
    cur.execute(query)

    alignTablesPath = os.path.abspath("dumpDBtables.py").split('QC8Test')[0] + 'QC8Test/src/Analysis/GEMQC8/data/StandAligmentTables/'
    outfile_name = alignTablesPath + "StandAlignmentValues_run{0}.csv".format(run_num)

    with open(outfile_name,"w+") as outfile:
        line = "POSITION,DX_cm,DY_cm,DZ_cm,RX_deg,RY_deg,RZ_deg,RUN_NUMBER\n"
        outfile.write(line)
        for result in cur:
            position   = result[0]
            dx         = result[1]
            dy         = result[2]
            dz         = result[3]
            rx         = result[4]
            ry         = result[5]
            rz         = result[6]
            run_number = result[7]
            line = str(position) + "," + str(dx) + "," + str(dy) + "," + str(dz) + "," + str(rx) + "," + str(ry) + "," + str(rz) + "," + str(run_number) + "\n"
            outfile.write(line)

    print "\nSuccesfully done!\n"

def getHotStripsTable(run_num):
    print "\nDownloading HotStripsTable for run {0}".format(run_num)

    db = cx_Oracle.connect('GEM_904_COND/904CondDB@INT2R')
    cur = db.cursor()

    query = "select * from CMS_GEM_MUON_VIEW.QC8_GEM_MASKED_STRIPS_HOT_V_RH where RUN_NUMBER="+str(run_num)
    cur.execute(query)

    hotStripsTablesPath = os.path.abspath("dumpDBtables.py").split('QC8Test')[0] + 'QC8Test/src/Analysis/GEMQC8/data/HotStripsTables/'
    outfile_name = hotStripsTablesPath + "HotStrips_run{0}.csv".format(run_num)

    with open(outfile_name,"w+") as outfile:
        line = "CH_SERIAL_NUMBER,GEM_NUMBER,POSITION,VFAT,CHANNEL,STRIP,RUN_NUMBER\n"
        outfile.write(line)
        for result in cur:
            chamber_name = result[0]
            gem_num      = result[1]
            position     = result[2]
            vfat         = result[3]
            channel      = result[4]
            strip        = result[5]
            run_number   = result[6]
            line = str(chamber_name) + "," + str(gem_num) + "," + str(position) + "," + str(vfat) + "," + str(channel) + "," + str(strip) + "," + str(run_number) + "\n"
            outfile.write(line)

    print "\nSuccesfully done!\n"

def getDeadStripsTable(run_num):
    print "\nDownloading DeadStripsTable for run {0}".format(run_num)

    db = cx_Oracle.connect('GEM_904_COND/904CondDB@INT2R')
    cur = db.cursor()

    query = "select * from CMS_GEM_MUON_VIEW.QC8_GEM_MASKED_STRIPS_DEAD_V_RH where RUN_NUMBER="+str(run_num)
    cur.execute(query)

    deadStripsTablesPath = os.path.abspath("dumpDBtables.py").split('QC8Test')[0] + 'QC8Test/src/Analysis/GEMQC8/data/DeadStripsTables/'
    outfile_name = deadStripsTablesPath + "DeadStrips_run{0}.csv".format(run_num)

    with open(outfile_name,"w+") as outfile:
        line = "CH_SERIAL_NUMBER,GEM_NUMBER,POSITION,VFAT,CHANNEL,STRIP,RUN_NUMBER\n"
        outfile.write(line)
        for result in cur:
            chamber_name = result[0]
            gem_num      = result[1]
            position     = result[2]
            vfat         = result[3]
            channel      = result[4]
            strip        = result[5]
            run_number   = result[6]
            line = str(chamber_name) + "," + str(gem_num) + "," + str(position) + "," + str(vfat) + "," + str(channel) + "," + str(strip) + "," + str(run_number) + "\n"
            outfile.write(line)

    print "\nSuccesfully done!\n"

if __name__ == '__main__':
    runNumber = sys.argv[1]
    tableType = sys.argv[2]
    if tableType == "ConfigurationTable":
        getConfigurationTable(runNumber)
    elif tableType == "AlignmentTable":
        getAlignmentTable(runNumber)
    elif tableType == "HotStripsTable":
        getHotStripsTable(runNumber)
    elif tableType == "DeadStripsTable":
        getDeadStripsTable(runNumber)
    else:
        print "Wrong name for a table!"
