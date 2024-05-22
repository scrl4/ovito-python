# /* 旨在运用ovito python 去处理RDF */
# /* 如有疑问参考https://docs.ovito.org/python/introduction/file_io.html          */
# /* 或者https://docs.ovito.org/reference/pipelines/modifiers/time_averaging.html */
# --------------------------------------------- 
# 导入相关包
from ovito.io import import_file, export_file
from ovito.modifiers import CoordinationAnalysisModifier,TimeAveragingModifier
# 导入文件，可导入多个文件
pipeline = import_file('C:\\Users\\Z\\Desktop\\XDATCAR (3)')
# 输出原子种类
for t in pipeline.compute().particles.particle_types.types:
    print("Type %i:%s"%(t.id,t.name))
# 输出帧数     
print("一共有{0}帧".format(pipeline.source.num_frames))
# 添加RDF修饰符,partial是所有, only_selected是只选择--Ture/False
modifier = CoordinationAnalysisModifier(cutoff=20,number_of_bins=200,partial=True)
pipeline.modifiers.append(modifier)
# 添加时间平均修饰符,interval是起始与终止值，sampling_frequency是间隔
pipeline.modifiers.append(TimeAveragingModifier(operate_on='table:coordination-rdf',interval=(5000,6000),sampling_frequency=1))
# 输出平均RDF
export_file(pipeline,"rdf.txt","txt/table",key="coordination-rdf[average]")