# -*- coding: utf8 -*-
# Copyright (c) 2017-2021 THL A29 Limited, a Tencent company. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import warnings

from tencentcloud.common.abstract_model import AbstractModel


class AccountInfo(AbstractModel):
    """账户信息

    """

    def __init__(self):
        r"""
        :param DBInstanceId: 实例ID，形如postgres-lnp6j617
        :type DBInstanceId: str
        :param UserName: 帐号
        :type UserName: str
        :param Remark: 帐号备注
        :type Remark: str
        :param Status: 帐号状态。 1-创建中，2-正常，3-修改中，4-密码重置中，-1-删除中
        :type Status: int
        :param CreateTime: 帐号创建时间
        :type CreateTime: str
        :param UpdateTime: 帐号最后一次更新时间
        :type UpdateTime: str
        """
        self.DBInstanceId = None
        self.UserName = None
        self.Remark = None
        self.Status = None
        self.CreateTime = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.DBInstanceId = params.get("DBInstanceId")
        self.UserName = params.get("UserName")
        self.Remark = params.get("Remark")
        self.Status = params.get("Status")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddDBInstanceToReadOnlyGroupRequest(AbstractModel):
    """AddDBInstanceToReadOnlyGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param DBInstanceId: 实例ID
        :type DBInstanceId: str
        :param ReadOnlyGroupId: 只读组ID
        :type ReadOnlyGroupId: str
        """
        self.DBInstanceId = None
        self.ReadOnlyGroupId = None


    def _deserialize(self, params):
        self.DBInstanceId = params.get("DBInstanceId")
        self.ReadOnlyGroupId = params.get("ReadOnlyGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddDBInstanceToReadOnlyGroupResponse(AbstractModel):
    """AddDBInstanceToReadOnlyGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param FlowId: 流程ID
        :type FlowId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.FlowId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        self.RequestId = params.get("RequestId")


class AnalysisItems(AbstractModel):
    """慢查询分析接口返回的分析详情，按照参数抽象之后进行分类

    """

    def __init__(self):
        r"""
        :param DatabaseName: 慢SQL查询的数据库名
        :type DatabaseName: str
        :param UserName: 慢SQL执行的用户名
        :type UserName: str
        :param NormalQuery: 抽象参数之后的慢SQL
        :type NormalQuery: str
        :param ClientAddr: 慢SQL执行的客户端地址
        :type ClientAddr: str
        :param CallNum: 在选定时间范围内慢SQL语句执行的次数
        :type CallNum: int
        :param CallPercent: 在选定时间范围内，慢SQL语句执行的次数占所有慢SQL的比例（小数返回）
        :type CallPercent: float
        :param CostTime: 在选定时间范围内，慢SQL执行的总时间
        :type CostTime: float
        :param CostPercent: 在选定时间范围内，慢SQL语句执行的总时间占所有慢SQL的比例（小数返回）
        :type CostPercent: float
        :param MinCostTime: 在选定时间范围内，慢SQL语句执行的耗时最短的时间（单位：ms）
        :type MinCostTime: float
        :param MaxCostTime: 在选定时间范围内，慢SQL语句执行的耗时最长的时间（单位：ms）
        :type MaxCostTime: float
        :param AvgCostTime: 在选定时间范围内，慢SQL语句执行的耗时平均时间（单位：ms）
        :type AvgCostTime: float
        :param FirstTime: 在选定时间范围内，慢SQL第一条开始执行的时间戳
        :type FirstTime: str
        :param LastTime: 在选定时间范围内，慢SQL最后一条开始执行的时间戳
        :type LastTime: str
        """
        self.DatabaseName = None
        self.UserName = None
        self.NormalQuery = None
        self.ClientAddr = None
        self.CallNum = None
        self.CallPercent = None
        self.CostTime = None
        self.CostPercent = None
        self.MinCostTime = None
        self.MaxCostTime = None
        self.AvgCostTime = None
        self.FirstTime = None
        self.LastTime = None


    def _deserialize(self, params):
        self.DatabaseName = params.get("DatabaseName")
        self.UserName = params.get("UserName")
        self.NormalQuery = params.get("NormalQuery")
        self.ClientAddr = params.get("ClientAddr")
        self.CallNum = params.get("CallNum")
        self.CallPercent = params.get("CallPercent")
        self.CostTime = params.get("CostTime")
        self.CostPercent = params.get("CostPercent")
        self.MinCostTime = params.get("MinCostTime")
        self.MaxCostTime = params.get("MaxCostTime")
        self.AvgCostTime = params.get("AvgCostTime")
        self.FirstTime = params.get("FirstTime")
        self.LastTime = params.get("LastTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BackupDownloadRestriction(AbstractModel):
    """备份下载限制信息

    """

    def __init__(self):
        r"""
        :param RestrictionType: 备份文件下载限制类型，NONE 无限制，内外网都可以下载；INTRANET 只允许内网下载；CUSTOMIZE 自定义限制下载的vpc或ip。
        :type RestrictionType: str
        :param VpcRestrictionEffect: vpc限制效力，ALLOW 允许；DENY 拒绝。
        :type VpcRestrictionEffect: str
        :param VpcIdSet: 允许或拒绝下载备份文件的vpcId列表。
        :type VpcIdSet: list of str
        :param IpRestrictionEffect: ip限制效力，ALLOW 允许；DENY 拒绝。
        :type IpRestrictionEffect: str
        :param IpSet: 允许或拒绝下载备份文件的ip列表。
        :type IpSet: list of str
        """
        self.RestrictionType = None
        self.VpcRestrictionEffect = None
        self.VpcIdSet = None
        self.IpRestrictionEffect = None
        self.IpSet = None


    def _deserialize(self, params):
        self.RestrictionType = params.get("RestrictionType")
        self.VpcRestrictionEffect = params.get("VpcRestrictionEffect")
        self.VpcIdSet = params.get("VpcIdSet")
        self.IpRestrictionEffect = params.get("IpRestrictionEffect")
        self.IpSet = params.get("IpSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BackupPlan(AbstractModel):
    """备份计划

    """

    def __init__(self):
        r"""
        :param BackupPeriod: 备份周期
        :type BackupPeriod: str
        :param BaseBackupRetentionPeriod: 基础备份保留时长
        :type BaseBackupRetentionPeriod: int
        :param MinBackupStartTime: 开始备份的最早时间
        :type MinBackupStartTime: str
        :param MaxBackupStartTime: 开始备份的最晚时间
        :type MaxBackupStartTime: str
        """
        self.BackupPeriod = None
        self.BaseBackupRetentionPeriod = None
        self.MinBackupStartTime = None
        self.MaxBackupStartTime = None


    def _deserialize(self, params):
        self.BackupPeriod = params.get("BackupPeriod")
        self.BaseBackupRetentionPeriod = params.get("BaseBackupRetentionPeriod")
        self.MinBackupStartTime = params.get("MinBackupStartTime")
        self.MaxBackupStartTime = params.get("MaxBackupStartTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BackupSummary(AbstractModel):
    """实例备份统计项

    """

    def __init__(self):
        r"""
        :param DBInstanceId: 实例ID。
        :type DBInstanceId: str
        :param LogBackupCount: 实例日志备份数量。
        :type LogBackupCount: int
        :param LogBackupSize: 实例日志备份大小。
        :type LogBackupSize: int
        :param ManualBaseBackupCount: 手动创建的实例基础备份数量。
        :type ManualBaseBackupCount: int
        :param ManualBaseBackupSize: 手动创建的实例基础备份大小。
        :type ManualBaseBackupSize: int
        :param AutoBaseBackupCount: 自动创建的实例基础备份数量。
        :type AutoBaseBackupCount: int
        :param AutoBaseBackupSize: 自动创建的实例基础备份大小。
        :type AutoBaseBackupSize: int
        :param TotalBackupCount: 总备份数量
        :type TotalBackupCount: int
        :param TotalBackupSize: 总备份大小
        :type TotalBackupSize: int
        """
        self.DBInstanceId = None
        self.LogBackupCount = None
        self.LogBackupSize = None
        self.ManualBaseBackupCount = None
        self.ManualBaseBackupSize = None
        self.AutoBaseBackupCount = None
        self.AutoBaseBackupSize = None
        self.TotalBackupCount = None
        self.TotalBackupSize = None


    def _deserialize(self, params):
        self.DBInstanceId = params.get("DBInstanceId")
        self.LogBackupCount = params.get("LogBackupCount")
        self.LogBackupSize = params.get("LogBackupSize")
        self.ManualBaseBackupCount = params.get("ManualBaseBackupCount")
        self.ManualBaseBackupSize = params.get("ManualBaseBackupSize")
        self.AutoBaseBackupCount = params.get("AutoBaseBackupCount")
        self.AutoBaseBackupSize = params.get("AutoBaseBackupSize")
        self.TotalBackupCount = params.get("TotalBackupCount")
        self.TotalBackupSize = params.get("TotalBackupSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BaseBackup(AbstractModel):
    """数据库基础备份信息

    """

    def __init__(self):
        r"""
        :param DBInstanceId: 实例ID。
        :type DBInstanceId: str
        :param Id: 备份文件唯一标识。
        :type Id: str
        :param Name: 备份文件名称。
        :type Name: str
        :param BackupMethod: 备份方式：物理备份、逻辑备份。
        :type BackupMethod: str
        :param BackupMode: 备份模式：自动备份、手动备份。
        :type BackupMode: str
        :param State: 备份任务状态。
        :type State: str
        :param Size: 备份集大小，单位bytes。
        :type Size: int
        :param StartTime: 备份的开始时间。
        :type StartTime: str
        :param FinishTime: 备份的结束时间。
        :type FinishTime: str
        :param ExpireTime: 备份的过期时间。
        :type ExpireTime: str
        """
        self.DBInstanceId = None
        self.Id = None
        self.Name = None
        self.BackupMethod = None
        self.BackupMode = None
        self.State = None
        self.Size = None
        self.StartTime = None
        self.FinishTime = None
        self.ExpireTime = None


    def _deserialize(self, params):
        self.DBInstanceId = params.get("DBInstanceId")
        self.Id = params.get("Id")
        self.Name = params.get("Name")
        self.BackupMethod = params.get("BackupMethod")
        self.BackupMode = params.get("BackupMode")
        self.State = params.get("State")
        self.Size = params.get("Size")
        self.StartTime = params.get("StartTime")
        self.FinishTime = params.get("FinishTime")
        self.ExpireTime = params.get("ExpireTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClassInfo(AbstractModel):
    """数据库实例规格

    """

    def __init__(self):
        r"""
        :param SpecCode: 规格ID
        :type SpecCode: str
        :param CPU: CPU核数
        :type CPU: int
        :param Memory: 内存大小，单位：MB
        :type Memory: int
        :param MaxStorage: 该规格所支持最大存储容量，单位：GB
        :type MaxStorage: int
        :param MinStorage: 该规格所支持最小存储容量，单位：GB
        :type MinStorage: int
        :param QPS: 该规格的预估QPS
        :type QPS: int
        """
        self.SpecCode = None
        self.CPU = None
        self.Memory = None
        self.MaxStorage = None
        self.MinStorage = None
        self.QPS = None


    def _deserialize(self, params):
        self.SpecCode = params.get("SpecCode")
        self.CPU = params.get("CPU")
        self.Memory = params.get("Memory")
        self.MaxStorage = params.get("MaxStorage")
        self.MinStorage = params.get("MinStorage")
        self.QPS = params.get("QPS")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloneDBInstanceRequest(AbstractModel):
    """CloneDBInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param DBInstanceId: 克隆的源实例ID。
        :type DBInstanceId: str
        :param SpecCode: 售卖规格ID。该参数可以通过调用DescribeProductConfig的返回值中的SpecCode字段来获取。
        :type SpecCode: str
        :param Storage: 实例容量大小，单位：GB。
        :type Storage: int
        :param Period: 购买时长，单位：月。目前只支持1,2,3,4,5,6,7,8,9,10,11,12,24,36这些值，按量计费模式下该参数传1。
        :type Period: int
        :param AutoRenewFlag: 续费标记：0-正常续费（默认）；1-自动续费。
        :type AutoRenewFlag: int
        :param VpcId: 私有网络ID。
        :type VpcId: str
        :param SubnetId: 已配置的私有网络中的子网ID。
        :type SubnetId: str
        :param Name: 新购实例的实例名称。
        :type Name: str
        :param InstanceChargeType: 实例计费类型。目前支持：PREPAID（预付费，即包年包月），POSTPAID_BY_HOUR（后付费，即按量计费）。
        :type InstanceChargeType: str
        :param SecurityGroupIds: 安全组ID。
        :type SecurityGroupIds: list of str
        :param ProjectId: 项目ID。
        :type ProjectId: int
        :param TagList: 实例需要绑定的Tag信息，默认为空。
        :type TagList: list of Tag
        :param DBNodeSet: 购买多可用区实例时填写。
        :type DBNodeSet: list of DBNode
        :param AutoVoucher: 是否自动使用代金券。1（是），0（否），默认不使用。
        :type AutoVoucher: int
        :param VoucherIds: 代金券ID列表。
        :type VoucherIds: str
        :param ActivityId: 活动ID。
        :type ActivityId: int
        :param BackupSetId: 基础备份集ID。
        :type BackupSetId: str
        :param RecoveryTargetTime: 恢复时间点。
        :type RecoveryTargetTime: str
        """
        self.DBInstanceId = None
        self.SpecCode = None
        self.Storage = None
        self.Period = None
        self.AutoRenewFlag = None
        self.VpcId = None
        self.SubnetId = None
        self.Name = None
        self.InstanceChargeType = None
        self.SecurityGroupIds = None
        self.ProjectId = None
        self.TagList = None
        self.DBNodeSet = None
        self.AutoVoucher = None
        self.VoucherIds = None
        self.ActivityId = None
        self.BackupSetId = None
        self.RecoveryTargetTime = None


    def _deserialize(self, params):
        self.DBInstanceId = params.get("DBInstanceId")
        self.SpecCode = params.get("SpecCode")
        self.Storage = params.get("Storage")
        self.Period = params.get("Period")
        self.AutoRenewFlag = params.get("AutoRenewFlag")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.Name = params.get("Name")
        self.InstanceChargeType = params.get("InstanceChargeType")
        self.SecurityGroupIds = params.get("SecurityGroupIds")
        self.ProjectId = params.get("ProjectId")
        if params.get("TagList") is not None:
            self.TagList = []
            for item in params.get("TagList"):
                obj = Tag()
                obj._deserialize(item)
                self.TagList.append(obj)
        if params.get("DBNodeSet") is not None:
            self.DBNodeSet = []
            for item in params.get("DBNodeSet"):
                obj = DBNode()
                obj._deserialize(item)
                self.DBNodeSet.append(obj)
        self.AutoVoucher = params.get("AutoVoucher")
        self.VoucherIds = params.get("VoucherIds")
        self.ActivityId = params.get("ActivityId")
        self.BackupSetId = params.get("BackupSetId")
        self.RecoveryTargetTime = params.get("RecoveryTargetTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloneDBInstanceResponse(AbstractModel):
    """CloneDBInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param DealName: 订单号。
注意：此字段可能返回 null，表示取不到有效值。
        :type DealName: str
        :param BillId: 订单流水号。
注意：此字段可能返回 null，表示取不到有效值。
        :type BillId: str
        :param DBInstanceId: 克隆出的新实例ID，当前只支持后付费返回该值。
注意：此字段可能返回 null，表示取不到有效值。
        :type DBInstanceId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DealName = None
        self.BillId = None
        self.DBInstanceId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DealName = params.get("DealName")
        self.BillId = params.get("BillId")
        self.DBInstanceId = params.get("DBInstanceId")
        self.RequestId = params.get("RequestId")


class CloseDBExtranetAccessRequest(AbstractModel):
    """CloseDBExtranetAccess请求参数结构体

    """

    def __init__(self):
        r"""
        :param DBInstanceId: 实例ID，形如postgres-6r233v55
        :type DBInstanceId: str
        :param IsIpv6: 是否关闭Ipv6外网，1：是，0：否
        :type IsIpv6: int
        """
        self.DBInstanceId = None
        self.IsIpv6 = None


    def _deserialize(self, params):
        self.DBInstanceId = params.get("DBInstanceId")
        self.IsIpv6 = params.get("IsIpv6")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloseDBExtranetAccessResponse(AbstractModel):
    """CloseDBExtranetAccess返回参数结构体

    """

    def __init__(self):
        r"""
        :param FlowId: 异步任务流程ID
        :type FlowId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.FlowId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        self.RequestId = params.get("RequestId")


class CloseServerlessDBExtranetAccessRequest(AbstractModel):
    """CloseServerlessDBExtranetAccess请求参数结构体

    """

    def __init__(self):
        r"""
        :param DBInstanceId: 实例唯一标识符
        :type DBInstanceId: str
        :param DBInstanceName: 实例名称
        :type DBInstanceName: str
        """
        self.DBInstanceId = None
        self.DBInstanceName = None


    def _deserialize(self, params):
        self.DBInstanceId = params.get("DBInstanceId")
        self.DBInstanceName = params.get("DBInstanceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloseServerlessDBExtranetAccessResponse(AbstractModel):
    """CloseServerlessDBExtranetAccess返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateBaseBackupRequest(AbstractModel):
    """CreateBaseBackup请求参数结构体

    """

    def __init__(self):
        r"""
        :param DBInstanceId: 实例ID。
        :type DBInstanceId: str
        """
        self.DBInstanceId = None


    def _deserialize(self, params):
        self.DBInstanceId = params.get("DBInstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateBaseBackupResponse(AbstractModel):
    """CreateBaseBackup返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateDBInstanceNetworkAccessRequest(AbstractModel):
    """CreateDBInstanceNetworkAccess请求参数结构体

    """

    def __init__(self):
        r"""
        :param DBInstanceId: 实例ID，形如：postgres-6bwgamo3。
        :type DBInstanceId: str
        :param VpcId: 私有网络统一 ID。
        :type VpcId: str
        :param SubnetId: 子网ID。
        :type SubnetId: str
        :param IsAssignVip: 是否指定分配vip true-指定分配  false-自动分配。
        :type IsAssignVip: bool
        :param Vip: 目标VIP地址。
        :type Vip: str
        """
        self.DBInstanceId = None
        self.VpcId = None
        self.SubnetId = None
        self.IsAssignVip = None
        self.Vip = None


    def _deserialize(self, params):
        self.DBInstanceId = params.get("DBInstanceId")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.IsAssignVip = params.get("IsAssignVip")
        self.Vip = params.get("Vip")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDBInstanceNetworkAccessResponse(AbstractModel):
    """CreateDBInstanceNetworkAccess返回参数结构体

    """

    def __init__(self):
        r"""
        :param FlowId: 流程ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type FlowId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.FlowId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        self.RequestId = params.get("RequestId")


class CreateDBInstancesRequest(AbstractModel):
    """CreateDBInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param SpecCode: 售卖规格ID。该参数可以通过调用DescribeProductConfig的返回值中的SpecCode字段来获取。
        :type SpecCode: str
        :param Storage: 实例容量大小，单位：GB。
        :type Storage: int
        :param InstanceCount: 一次性购买的实例数量。取值1-100
        :type InstanceCount: int
        :param Period: 购买时长，单位：月。目前只支持1,2,3,4,5,6,7,8,9,10,11,12,24,36这些值，按量计费模式下该参数传1。
        :type Period: int
        :param Zone: 可用区ID。该参数可以通过调用 DescribeZones 接口的返回值中的Zone字段来获取。
        :type Zone: str
        :param ProjectId: 项目ID。
        :type ProjectId: int
        :param DBVersion: PostgreSQL版本。当输入该参数时，会基于此版本创建对应的最新内核版本号实例。该参数和DBMajorVersion、DBKernelVersion至少需要传递一个。
        :type DBVersion: str
        :param InstanceChargeType: 实例计费类型。目前支持：PREPAID（预付费，即包年包月），POSTPAID_BY_HOUR（后付费，即按量计费）。
        :type InstanceChargeType: str
        :param AutoVoucher: 是否自动使用代金券。1（是），0（否），默认不使用。
        :type AutoVoucher: int
        :param VoucherIds: 代金券ID列表，目前仅支持指定一张代金券。
        :type VoucherIds: list of str
        :param VpcId: 私有网络ID。
        :type VpcId: str
        :param SubnetId: 私有网络子网ID。
        :type SubnetId: str
        :param AutoRenewFlag: 续费标记：0-正常续费（默认）；1-自动续费；
        :type AutoRenewFlag: int
        :param ActivityId: 活动ID
        :type ActivityId: int
        :param Name: 实例名(后续支持)
        :type Name: str
        :param NeedSupportIpv6: 是否需要支持Ipv6，1：是，0：否
        :type NeedSupportIpv6: int
        :param TagList: 实例需要绑定的Tag信息，默认为空
        :type TagList: list of Tag
        :param SecurityGroupIds: 安全组id
        :type SecurityGroupIds: list of str
        :param DBMajorVersion: PostgreSQL主要版本。当输入该参数时，会基于此版本创建对应的最新内核版本号实例。该参数和DBVersion、DBKernelVersion至少需要传递一个。
        :type DBMajorVersion: str
        :param DBKernelVersion: PostgreSQL内核版本。当输入该参数时，会创建该内核版本号实例。该参数和DBVersion、DBMajorVersion至少需要传递一个。
        :type DBKernelVersion: str
        """
        self.SpecCode = None
        self.Storage = None
        self.InstanceCount = None
        self.Period = None
        self.Zone = None
        self.ProjectId = None
        self.DBVersion = None
        self.InstanceChargeType = None
        self.AutoVoucher = None
        self.VoucherIds = None
        self.VpcId = None
        self.SubnetId = None
        self.AutoRenewFlag = None
        self.ActivityId = None
        self.Name = None
        self.NeedSupportIpv6 = None
        self.TagList = None
        self.SecurityGroupIds = None
        self.DBMajorVersion = None
        self.DBKernelVersion = None


    def _deserialize(self, params):
        self.SpecCode = params.get("SpecCode")
        self.Storage = params.get("Storage")
        self.InstanceCount = params.get("InstanceCount")
        self.Period = params.get("Period")
        self.Zone = params.get("Zone")
        self.ProjectId = params.get("ProjectId")
        self.DBVersion = params.get("DBVersion")
        self.InstanceChargeType = params.get("InstanceChargeType")
        self.AutoVoucher = params.get("AutoVoucher")
        self.VoucherIds = params.get("VoucherIds")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.AutoRenewFlag = params.get("AutoRenewFlag")
        self.ActivityId = params.get("ActivityId")
        self.Name = params.get("Name")
        self.NeedSupportIpv6 = params.get("NeedSupportIpv6")
        if params.get("TagList") is not None:
            self.TagList = []
            for item in params.get("TagList"):
                obj = Tag()
                obj._deserialize(item)
                self.TagList.append(obj)
        self.SecurityGroupIds = params.get("SecurityGroupIds")
        self.DBMajorVersion = params.get("DBMajorVersion")
        self.DBKernelVersion = params.get("DBKernelVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDBInstancesResponse(AbstractModel):
    """CreateDBInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param DealNames: 订单号列表。每个实例对应一个订单号。
        :type DealNames: list of str
        :param BillId: 冻结流水号
        :type BillId: str
        :param DBInstanceIdSet: 创建成功的实例ID集合，只在后付费情景下有返回值
        :type DBInstanceIdSet: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DealNames = None
        self.BillId = None
        self.DBInstanceIdSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DealNames = params.get("DealNames")
        self.BillId = params.get("BillId")
        self.DBInstanceIdSet = params.get("DBInstanceIdSet")
        self.RequestId = params.get("RequestId")


class CreateInstancesRequest(AbstractModel):
    """CreateInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param SpecCode: 售卖规格ID。该参数可以通过调用DescribeProductConfig的返回值中的SpecCode字段来获取。
        :type SpecCode: str
        :param Storage: 实例容量大小，单位：GB。
        :type Storage: int
        :param InstanceCount: 一次性购买的实例数量。取值1-10。
        :type InstanceCount: int
        :param Period: 购买时长，单位：月。目前只支持1,2,3,4,5,6,7,8,9,10,11,12,24,36这些值，按量计费模式下该参数传1。
        :type Period: int
        :param Zone: 可用区ID。该参数可以通过调用 DescribeZones 接口的返回值中的Zone字段来获取。
        :type Zone: str
        :param Charset: 实例字符集，目前只支持：UTF8、LATIN1。
        :type Charset: str
        :param AdminName: 实例根账号用户名。
        :type AdminName: str
        :param AdminPassword: 实例根账号用户名对应的密码。
        :type AdminPassword: str
        :param ProjectId: 项目ID。
        :type ProjectId: int
        :param DBVersion: PostgreSQL版本。当输入该参数时，会基于此版本创建对应的最新内核版本号实例。该参数和DBMajorVersion、DBKernelVersion至少需要传递一个。
        :type DBVersion: str
        :param InstanceChargeType: 实例计费类型。目前支持：PREPAID（预付费，即包年包月），POSTPAID_BY_HOUR（后付费，即按量计费）。
        :type InstanceChargeType: str
        :param AutoVoucher: 是否自动使用代金券。1（是），0（否），默认不使用。
        :type AutoVoucher: int
        :param VoucherIds: 代金券ID列表，目前仅支持指定一张代金券。
        :type VoucherIds: list of str
        :param VpcId: 私有网络ID。
        :type VpcId: str
        :param SubnetId: 已配置的私有网络中的子网ID。
        :type SubnetId: str
        :param AutoRenewFlag: 续费标记：0-正常续费（默认）；1-自动续费。
        :type AutoRenewFlag: int
        :param ActivityId: 活动ID。
        :type ActivityId: int
        :param Name: 实例名。
        :type Name: str
        :param NeedSupportIpv6: 是否需要支持Ipv6，1：是，0：否（默认）。
        :type NeedSupportIpv6: int
        :param TagList: 实例需要绑定的Tag信息，默认为空。
        :type TagList: list of Tag
        :param SecurityGroupIds: 安全组ID。
        :type SecurityGroupIds: list of str
        :param DBMajorVersion: PostgreSQL主要版本。目前支持10，11，12，13这几个版本。当输入该参数时，会基于此版本创建对应的最新内核版本号实例。该参数和DBVersion、DBKernelVersion至少需要传递一个。
        :type DBMajorVersion: str
        :param DBKernelVersion: PostgreSQL内核版本。当输入该参数时，会创建该内核版本号实例。该参数和DBVersion、DBMajorVersion至少需要传递一个。
        :type DBKernelVersion: str
        :param DBNodeSet: 实例节点信息，购买跨可用区实例时填写。
        :type DBNodeSet: list of DBNode
        :param NeedSupportTDE: 是否需要支持数据透明加密，1：是，0：否（默认）。
        :type NeedSupportTDE: int
        :param KMSKeyId: 自定义密钥的KeyId，若选择自定义密匙加密，则需要传入自定义密匙的KeyId，KeyId是CMK的唯一标识。
        :type KMSKeyId: str
        :param KMSRegion: 使用KMS服务的地域，KMSRegion为空默认使用本地域的KMS，本地域不支持的情况下需自选其他KMS支持的地域。
        :type KMSRegion: str
        :param DBEngine: 数据库引擎，支持：
1、postgresql（云数据库PostgreSQL）；
2、mssql_compatible（MSSQL兼容-云数据库PostgreSQL）；
如不指定默认使用postgresql。
        :type DBEngine: str
        :param DBEngineConfig: 数据库引擎的配置信息，配置格式如下：
{"$key1":"$value1", "$key2":"$value2"}

各引擎支持如下：
1、mssql_compatible引擎：
migrationMode：数据库模式，可选参数，可取值：single-db（单数据库模式），multi-db（多数据库模式）。默认为single-db。
defaultLocale：排序区域规则，可选参数，在初始化后不可修改，默认为en_US，可选值如下：
"af_ZA", "sq_AL", "ar_DZ", "ar_BH", "ar_EG", "ar_IQ", "ar_JO", "ar_KW", "ar_LB", "ar_LY", "ar_MA", "ar_OM", "ar_QA", "ar_SA", "ar_SY", "ar_TN", "ar_AE", "ar_YE", "hy_AM", "az_Cyrl_AZ", "az_Latn_AZ", "eu_ES", "be_BY", "bg_BG", "ca_ES", "zh_HK", "zh_MO", "zh_CN", "zh_SG", "zh_TW", "hr_HR", "cs_CZ", "da_DK", "nl_BE", "nl_NL", "en_AU", "en_BZ", "en_CA", "en_IE", "en_JM", "en_NZ", "en_PH", "en_ZA", "en_TT", "en_GB", "en_US", "en_ZW", "et_EE", "fo_FO", "fa_IR", "fi_FI", "fr_BE", "fr_CA", "fr_FR", "fr_LU", "fr_MC", "fr_CH", "mk_MK", "ka_GE", "de_AT", "de_DE", "de_LI", "de_LU", "de_CH", "el_GR", "gu_IN", "he_IL", "hi_IN", "hu_HU", "is_IS", "id_ID", "it_IT", "it_CH", "ja_JP", "kn_IN", "kok_IN", "ko_KR", "ky_KG", "lv_LV", "lt_LT", "ms_BN", "ms_MY", "mr_IN", "mn_MN", "nb_NO", "nn_NO", "pl_PL", "pt_BR", "pt_PT", "pa_IN", "ro_RO", "ru_RU", "sa_IN", "sr_Cyrl_RS", "sr_Latn_RS", "sk_SK", "sl_SI", "es_AR", "es_BO", "es_CL", "es_CO", "es_CR", "es_DO", "es_EC", "es_SV", "es_GT", "es_HN", "es_MX", "es_NI", "es_PA", "es_PY","es_PE", "es_PR", "es_ES", "es_TRADITIONAL", "es_UY", "es_VE", "sw_KE", "sv_FI", "sv_SE", "tt_RU", "te_IN", "th_TH", "tr_TR", "uk_UA", "ur_IN", "ur_PK", "uz_Cyrl_UZ", "uz_Latn_UZ", "vi_VN"。
serverCollationName：排序规则名称，可选参数，在初始化后不可修改，默认为sql_latin1_general_cp1_ci_as，可选值如下：
"bbf_unicode_general_ci_as", "bbf_unicode_cp1_ci_as", "bbf_unicode_CP1250_ci_as", "bbf_unicode_CP1251_ci_as", "bbf_unicode_cp1253_ci_as", "bbf_unicode_cp1254_ci_as", "bbf_unicode_cp1255_ci_as", "bbf_unicode_cp1256_ci_as", "bbf_unicode_cp1257_ci_as", "bbf_unicode_cp1258_ci_as", "bbf_unicode_cp874_ci_as", "sql_latin1_general_cp1250_ci_as", "sql_latin1_general_cp1251_ci_as", "sql_latin1_general_cp1_ci_as", "sql_latin1_general_cp1253_ci_as", "sql_latin1_general_cp1254_ci_as", "sql_latin1_general_cp1255_ci_as","sql_latin1_general_cp1256_ci_as", "sql_latin1_general_cp1257_ci_as", "sql_latin1_general_cp1258_ci_as", "chinese_prc_ci_as", "cyrillic_general_ci_as", "finnish_swedish_ci_as", "french_ci_as", "japanese_ci_as", "korean_wansung_ci_as", "latin1_general_ci_as", "modern_spanish_ci_as", "polish_ci_as", "thai_ci_as", "traditional_spanish_ci_as", "turkish_ci_as", "ukrainian_ci_as", "vietnamese_ci_as"。
        :type DBEngineConfig: str
        """
        self.SpecCode = None
        self.Storage = None
        self.InstanceCount = None
        self.Period = None
        self.Zone = None
        self.Charset = None
        self.AdminName = None
        self.AdminPassword = None
        self.ProjectId = None
        self.DBVersion = None
        self.InstanceChargeType = None
        self.AutoVoucher = None
        self.VoucherIds = None
        self.VpcId = None
        self.SubnetId = None
        self.AutoRenewFlag = None
        self.ActivityId = None
        self.Name = None
        self.NeedSupportIpv6 = None
        self.TagList = None
        self.SecurityGroupIds = None
        self.DBMajorVersion = None
        self.DBKernelVersion = None
        self.DBNodeSet = None
        self.NeedSupportTDE = None
        self.KMSKeyId = None
        self.KMSRegion = None
        self.DBEngine = None
        self.DBEngineConfig = None


    def _deserialize(self, params):
        self.SpecCode = params.get("SpecCode")
        self.Storage = params.get("Storage")
        self.InstanceCount = params.get("InstanceCount")
        self.Period = params.get("Period")
        self.Zone = params.get("Zone")
        self.Charset = params.get("Charset")
        self.AdminName = params.get("AdminName")
        self.AdminPassword = params.get("AdminPassword")
        self.ProjectId = params.get("ProjectId")
        self.DBVersion = params.get("DBVersion")
        self.InstanceChargeType = params.get("InstanceChargeType")
        self.AutoVoucher = params.get("AutoVoucher")
        self.VoucherIds = params.get("VoucherIds")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.AutoRenewFlag = params.get("AutoRenewFlag")
        self.ActivityId = params.get("ActivityId")
        self.Name = params.get("Name")
        self.NeedSupportIpv6 = params.get("NeedSupportIpv6")
        if params.get("TagList") is not None:
            self.TagList = []
            for item in params.get("TagList"):
                obj = Tag()
                obj._deserialize(item)
                self.TagList.append(obj)
        self.SecurityGroupIds = params.get("SecurityGroupIds")
        self.DBMajorVersion = params.get("DBMajorVersion")
        self.DBKernelVersion = params.get("DBKernelVersion")
        if params.get("DBNodeSet") is not None:
            self.DBNodeSet = []
            for item in params.get("DBNodeSet"):
                obj = DBNode()
                obj._deserialize(item)
                self.DBNodeSet.append(obj)
        self.NeedSupportTDE = params.get("NeedSupportTDE")
        self.KMSKeyId = params.get("KMSKeyId")
        self.KMSRegion = params.get("KMSRegion")
        self.DBEngine = params.get("DBEngine")
        self.DBEngineConfig = params.get("DBEngineConfig")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateInstancesResponse(AbstractModel):
    """CreateInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param DealNames: 订单号列表。每个实例对应一个订单号。
        :type DealNames: list of str
        :param BillId: 冻结流水号。
        :type BillId: str
        :param DBInstanceIdSet: 创建成功的实例ID集合，只在后付费情景下有返回值。
        :type DBInstanceIdSet: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DealNames = None
        self.BillId = None
        self.DBInstanceIdSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DealNames = params.get("DealNames")
        self.BillId = params.get("BillId")
        self.DBInstanceIdSet = params.get("DBInstanceIdSet")
        self.RequestId = params.get("RequestId")


class CreateParameterTemplateRequest(AbstractModel):
    """CreateParameterTemplate请求参数结构体

    """

    def __init__(self):
        r"""
        :param TemplateName: 模板名称，长度为1～60个字符，仅支持数字,英文大小写字母、中文以及特殊字符_-./()（）[]+=：:@
        :type TemplateName: str
        :param DBMajorVersion: 数据库大版本号，例如：11，12，13
        :type DBMajorVersion: str
        :param DBEngine: 数据库引擎，例如：postgresql，mssql_compatible
        :type DBEngine: str
        :param TemplateDescription: 参数模板描述，长度为0～60个字符，仅支持数字,英文大小写字母、中文以及特殊字符_-./()（）[]+=：:@
        :type TemplateDescription: str
        """
        self.TemplateName = None
        self.DBMajorVersion = None
        self.DBEngine = None
        self.TemplateDescription = None


    def _deserialize(self, params):
        self.TemplateName = params.get("TemplateName")
        self.DBMajorVersion = params.get("DBMajorVersion")
        self.DBEngine = params.get("DBEngine")
        self.TemplateDescription = params.get("TemplateDescription")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateParameterTemplateResponse(AbstractModel):
    """CreateParameterTemplate返回参数结构体

    """

    def __init__(self):
        r"""
        :param TemplateId: 参数模板ID，用于唯一确认参数模板
        :type TemplateId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TemplateId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TemplateId = params.get("TemplateId")
        self.RequestId = params.get("RequestId")


class CreateReadOnlyDBInstanceRequest(AbstractModel):
    """CreateReadOnlyDBInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param SpecCode: 售卖规格ID。该参数可以通过调用DescribeProductConfig的返回值中的SpecCode字段来获取。
        :type SpecCode: str
        :param Storage: 实例容量大小，单位：GB。
        :type Storage: int
        :param InstanceCount: 一次性购买的实例数量。取值1-100
        :type InstanceCount: int
        :param Period: 购买时长，单位：月。目前只支持1,2,3,4,5,6,7,8,9,10,11,12,24,36这些值，按量计费模式下该参数传1。
        :type Period: int
        :param MasterDBInstanceId: 只读实例的主实例ID
        :type MasterDBInstanceId: str
        :param Zone: 可用区ID。该参数可以通过调用 DescribeZones 接口的返回值中的Zone字段来获取。
        :type Zone: str
        :param ProjectId: 项目ID。
        :type ProjectId: int
        :param DBVersion: 【废弃】不再需要指定，内核版本号与主实例保持一致
        :type DBVersion: str
        :param InstanceChargeType: 实例计费类型。目前支持：PREPAID（预付费，即包年包月），POSTPAID_BY_HOUR（后付费，即按量计费）。如果主实例为后付费，只读实例必须也为后付费。
        :type InstanceChargeType: str
        :param AutoVoucher: 是否自动使用代金券。1（是），0（否），默认不使用。
        :type AutoVoucher: int
        :param VoucherIds: 代金券ID列表，目前仅支持指定一张代金券。
        :type VoucherIds: list of str
        :param AutoRenewFlag: 续费标记：0-正常续费（默认）；1-自动续费；
        :type AutoRenewFlag: int
        :param VpcId: 私有网络ID。
        :type VpcId: str
        :param SubnetId: 私有网络子网ID。
        :type SubnetId: str
        :param ActivityId: 优惠活动ID
        :type ActivityId: int
        :param Name: 实例名(后续支持)
        :type Name: str
        :param NeedSupportIpv6: 是否需要支持Ipv6，1：是，0：否
        :type NeedSupportIpv6: int
        :param ReadOnlyGroupId: 只读组ID。
        :type ReadOnlyGroupId: str
        :param TagList: 实例需要绑定的Tag信息，默认为空（该类型为Tag数组类型）
        :type TagList: :class:`tencentcloud.postgres.v20170312.models.Tag`
        :param SecurityGroupIds: 安全组id
        :type SecurityGroupIds: list of str
        """
        self.SpecCode = None
        self.Storage = None
        self.InstanceCount = None
        self.Period = None
        self.MasterDBInstanceId = None
        self.Zone = None
        self.ProjectId = None
        self.DBVersion = None
        self.InstanceChargeType = None
        self.AutoVoucher = None
        self.VoucherIds = None
        self.AutoRenewFlag = None
        self.VpcId = None
        self.SubnetId = None
        self.ActivityId = None
        self.Name = None
        self.NeedSupportIpv6 = None
        self.ReadOnlyGroupId = None
        self.TagList = None
        self.SecurityGroupIds = None


    def _deserialize(self, params):
        self.SpecCode = params.get("SpecCode")
        self.Storage = params.get("Storage")
        self.InstanceCount = params.get("InstanceCount")
        self.Period = params.get("Period")
        self.MasterDBInstanceId = params.get("MasterDBInstanceId")
        self.Zone = params.get("Zone")
        self.ProjectId = params.get("ProjectId")
        self.DBVersion = params.get("DBVersion")
        self.InstanceChargeType = params.get("InstanceChargeType")
        self.AutoVoucher = params.get("AutoVoucher")
        self.VoucherIds = params.get("VoucherIds")
        self.AutoRenewFlag = params.get("AutoRenewFlag")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.ActivityId = params.get("ActivityId")
        self.Name = params.get("Name")
        self.NeedSupportIpv6 = params.get("NeedSupportIpv6")
        self.ReadOnlyGroupId = params.get("ReadOnlyGroupId")
        if params.get("TagList") is not None:
            self.TagList = Tag()
            self.TagList._deserialize(params.get("TagList"))
        self.SecurityGroupIds = params.get("SecurityGroupIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateReadOnlyDBInstanceResponse(AbstractModel):
    """CreateReadOnlyDBInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param DealNames: 订单号列表。每个实例对应一个订单号
        :type DealNames: list of str
        :param BillId: 冻结流水号
        :type BillId: str
        :param DBInstanceIdSet: 创建成功的实例ID集合，只在后付费情景下有返回值
        :type DBInstanceIdSet: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DealNames = None
        self.BillId = None
        self.DBInstanceIdSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DealNames = params.get("DealNames")
        self.BillId = params.get("BillId")
        self.DBInstanceIdSet = params.get("DBInstanceIdSet")
        self.RequestId = params.get("RequestId")


class CreateReadOnlyGroupNetworkAccessRequest(AbstractModel):
    """CreateReadOnlyGroupNetworkAccess请求参数结构体

    """

    def __init__(self):
        r"""
        :param ReadOnlyGroupId: RO组ID，形如：pgro-4t9c6g7k。
        :type ReadOnlyGroupId: str
        :param VpcId: 私有网络统一 ID。
        :type VpcId: str
        :param SubnetId: 子网ID。
        :type SubnetId: str
        :param IsAssignVip: 是否指定分配vip true-指定分配  false-自动分配。
        :type IsAssignVip: bool
        :param Vip: 目标VIP地址。
        :type Vip: str
        """
        self.ReadOnlyGroupId = None
        self.VpcId = None
        self.SubnetId = None
        self.IsAssignVip = None
        self.Vip = None


    def _deserialize(self, params):
        self.ReadOnlyGroupId = params.get("ReadOnlyGroupId")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.IsAssignVip = params.get("IsAssignVip")
        self.Vip = params.get("Vip")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateReadOnlyGroupNetworkAccessResponse(AbstractModel):
    """CreateReadOnlyGroupNetworkAccess返回参数结构体

    """

    def __init__(self):
        r"""
        :param FlowId: 流程ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type FlowId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.FlowId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        self.RequestId = params.get("RequestId")


class CreateReadOnlyGroupRequest(AbstractModel):
    """CreateReadOnlyGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param MasterDBInstanceId: 主实例ID
        :type MasterDBInstanceId: str
        :param Name: 只读组名称
        :type Name: str
        :param ProjectId: 项目ID
        :type ProjectId: int
        :param VpcId: 私有网络ID
        :type VpcId: str
        :param SubnetId: 子网ID
        :type SubnetId: str
        :param ReplayLagEliminate: 延迟时间大小开关：0关、1开
        :type ReplayLagEliminate: int
        :param ReplayLatencyEliminate: 延迟空间大小开关： 0关、1开
        :type ReplayLatencyEliminate: int
        :param MaxReplayLag: 延迟时间大小阈值，单位ms
        :type MaxReplayLag: int
        :param MaxReplayLatency: 延迟空间大小阈值，单位MB
        :type MaxReplayLatency: int
        :param MinDelayEliminateReserve: 延迟剔除最小保留实例数
        :type MinDelayEliminateReserve: int
        :param SecurityGroupIds: 安全组id
        :type SecurityGroupIds: list of str
        """
        self.MasterDBInstanceId = None
        self.Name = None
        self.ProjectId = None
        self.VpcId = None
        self.SubnetId = None
        self.ReplayLagEliminate = None
        self.ReplayLatencyEliminate = None
        self.MaxReplayLag = None
        self.MaxReplayLatency = None
        self.MinDelayEliminateReserve = None
        self.SecurityGroupIds = None


    def _deserialize(self, params):
        self.MasterDBInstanceId = params.get("MasterDBInstanceId")
        self.Name = params.get("Name")
        self.ProjectId = params.get("ProjectId")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.ReplayLagEliminate = params.get("ReplayLagEliminate")
        self.ReplayLatencyEliminate = params.get("ReplayLatencyEliminate")
        self.MaxReplayLag = params.get("MaxReplayLag")
        self.MaxReplayLatency = params.get("MaxReplayLatency")
        self.MinDelayEliminateReserve = params.get("MinDelayEliminateReserve")
        self.SecurityGroupIds = params.get("SecurityGroupIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateReadOnlyGroupResponse(AbstractModel):
    """CreateReadOnlyGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param ReadOnlyGroupId: 只读组ID
        :type ReadOnlyGroupId: str
        :param FlowId: 流程ID
注意：此字段可能返回 null，表示取不到有效值。
        :type FlowId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ReadOnlyGroupId = None
        self.FlowId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ReadOnlyGroupId = params.get("ReadOnlyGroupId")
        self.FlowId = params.get("FlowId")
        self.RequestId = params.get("RequestId")


class CreateServerlessDBInstanceRequest(AbstractModel):
    """CreateServerlessDBInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param Zone: 可用区ID。公测阶段仅支持ap-shanghai-2、ap-beijing-1,ap-guangzhou-2.
        :type Zone: str
        :param DBInstanceName: DB实例名称，同一个账号下该值必须唯一。
        :type DBInstanceName: str
        :param DBVersion: PostgreSQL内核版本，目前只支持：10.4。
        :type DBVersion: str
        :param DBCharset: PostgreSQL数据库字符集，目前支持UTF8。
        :type DBCharset: str
        :param ProjectId: 项目ID。
        :type ProjectId: int
        :param VpcId: 私有网络ID。
        :type VpcId: str
        :param SubnetId: 私有网络子网ID。
        :type SubnetId: str
        :param TagList: 实例需要绑定的标签数组信息
        :type TagList: list of Tag
        """
        self.Zone = None
        self.DBInstanceName = None
        self.DBVersion = None
        self.DBCharset = None
        self.ProjectId = None
        self.VpcId = None
        self.SubnetId = None
        self.TagList = None


    def _deserialize(self, params):
        self.Zone = params.get("Zone")
        self.DBInstanceName = params.get("DBInstanceName")
        self.DBVersion = params.get("DBVersion")
        self.DBCharset = params.get("DBCharset")
        self.ProjectId = params.get("ProjectId")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        if params.get("TagList") is not None:
            self.TagList = []
            for item in params.get("TagList"):
                obj = Tag()
                obj._deserialize(item)
                self.TagList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateServerlessDBInstanceResponse(AbstractModel):
    """CreateServerlessDBInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param DBInstanceId: 实例ID，该ID全局唯一，如：postgres-xxxxx
        :type DBInstanceId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DBInstanceId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DBInstanceId = params.get("DBInstanceId")
        self.RequestId = params.get("RequestId")


class DBBackup(AbstractModel):
    """数据库备份信息

    """

    def __init__(self):
        r"""
        :param Id: 备份文件唯一标识
        :type Id: int
        :param StartTime: 文件生成的开始时间
        :type StartTime: str
        :param EndTime: 文件生成的结束时间
        :type EndTime: str
        :param Size: 文件大小(K)
        :type Size: int
        :param Strategy: 策略（0-实例备份；1-多库备份）
        :type Strategy: int
        :param Way: 类型（0-定时）
        :type Way: int
        :param Type: 备份方式（1-完整）
        :type Type: int
        :param Status: 状态（1-创建中；2-成功；3-失败）
        :type Status: int
        :param DbList: DB列表
        :type DbList: list of str
        :param InternalAddr: 内网下载地址
        :type InternalAddr: str
        :param ExternalAddr: 外网下载地址
        :type ExternalAddr: str
        :param SetId: 备份集ID
注意：此字段可能返回 null，表示取不到有效值。
        :type SetId: str
        """
        self.Id = None
        self.StartTime = None
        self.EndTime = None
        self.Size = None
        self.Strategy = None
        self.Way = None
        self.Type = None
        self.Status = None
        self.DbList = None
        self.InternalAddr = None
        self.ExternalAddr = None
        self.SetId = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Size = params.get("Size")
        self.Strategy = params.get("Strategy")
        self.Way = params.get("Way")
        self.Type = params.get("Type")
        self.Status = params.get("Status")
        self.DbList = params.get("DbList")
        self.InternalAddr = params.get("InternalAddr")
        self.ExternalAddr = params.get("ExternalAddr")
        self.SetId = params.get("SetId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DBInstance(AbstractModel):
    """描述实例的详细信息

    """

    def __init__(self):
        r"""
        :param Region: 实例所属地域，如: ap-guangzhou，对应RegionSet的Region字段
        :type Region: str
        :param Zone: 实例所属可用区， 如：ap-guangzhou-3，对应ZoneSet的Zone字段
        :type Zone: str
        :param ProjectId: 项目ID
        :type ProjectId: int
        :param VpcId: 私有网络ID
        :type VpcId: str
        :param SubnetId: 子网ID
        :type SubnetId: str
        :param DBInstanceId: 实例ID
        :type DBInstanceId: str
        :param DBInstanceName: 实例名称
        :type DBInstanceName: str
        :param DBInstanceStatus: 实例状态，分别为：applying（申请中）、init(待初始化)、initing(初始化中)、running(运行中)、limited run（受限运行）、isolated（已隔离）、recycling（回收中）、recycled（已回收）、job running（任务执行中）、offline（下线）、migrating（迁移中）、expanding（扩容中）、waitSwitch（等待切换）、switching（切换中）、readonly（只读）、restarting（重启中）、network changing（网络变更中）、upgrading（内核版本升级中）
        :type DBInstanceStatus: str
        :param DBInstanceMemory: 实例分配的内存大小，单位：GB
        :type DBInstanceMemory: int
        :param DBInstanceStorage: 实例分配的存储空间大小，单位：GB
        :type DBInstanceStorage: int
        :param DBInstanceCpu: 实例分配的CPU数量，单位：个
        :type DBInstanceCpu: int
        :param DBInstanceClass: 售卖规格ID
        :type DBInstanceClass: str
        :param DBInstanceType: 实例类型，类型有：1、primary（主实例）；2、readonly（只读实例）；3、guard（灾备实例）；4、temp（临时实例）
        :type DBInstanceType: str
        :param DBInstanceVersion: 实例版本，目前只支持standard（双机高可用版, 一主一从）
        :type DBInstanceVersion: str
        :param DBCharset: 实例DB字符集
        :type DBCharset: str
        :param DBVersion: PostgreSQL版本
        :type DBVersion: str
        :param CreateTime: 实例创建时间
        :type CreateTime: str
        :param UpdateTime: 实例执行最后一次更新的时间
        :type UpdateTime: str
        :param ExpireTime: 实例到期时间
        :type ExpireTime: str
        :param IsolatedTime: 实例隔离时间
        :type IsolatedTime: str
        :param PayType: 计费模式，1、prepaid（包年包月,预付费）；2、postpaid（按量计费，后付费）
        :type PayType: str
        :param AutoRenew: 是否自动续费，1：自动续费，0：不自动续费
        :type AutoRenew: int
        :param DBInstanceNetInfo: 实例网络连接信息
        :type DBInstanceNetInfo: list of DBInstanceNetInfo
        :param Type: 机器类型
        :type Type: str
        :param AppId: 用户的AppId
        :type AppId: int
        :param Uid: 实例的Uid
        :type Uid: int
        :param SupportIpv6: 实例是否支持Ipv6，1：支持，0：不支持
        :type SupportIpv6: int
        :param TagList: 实例绑定的标签信息
注意：此字段可能返回 null，表示取不到有效值。
        :type TagList: list of Tag
        :param MasterDBInstanceId: 主实例信息，仅在实例为只读实例时返回
注意：此字段可能返回 null，表示取不到有效值。
        :type MasterDBInstanceId: str
        :param ReadOnlyInstanceNum: 只读实例数量
注意：此字段可能返回 null，表示取不到有效值。
        :type ReadOnlyInstanceNum: int
        :param StatusInReadonlyGroup: 只读实例在只读组中的状态
注意：此字段可能返回 null，表示取不到有效值。
        :type StatusInReadonlyGroup: str
        :param OfflineTime: 下线时间
注意：此字段可能返回 null，表示取不到有效值。
        :type OfflineTime: str
        :param DBKernelVersion: 数据库内核版本
注意：此字段可能返回 null，表示取不到有效值。
        :type DBKernelVersion: str
        :param NetworkAccessList: 实例网络信息列表（此字段已废弃）
注意：此字段可能返回 null，表示取不到有效值。
        :type NetworkAccessList: list of NetworkAccess
        :param DBMajorVersion: PostgreSQL主要版本
注意：此字段可能返回 null，表示取不到有效值。
        :type DBMajorVersion: str
        :param DBNodeSet: 实例的节点信息
注意：此字段可能返回 null，表示取不到有效值。
        :type DBNodeSet: list of DBNode
        :param IsSupportTDE: 实例是否支持TDE数据加密  0：不支持，1：支持
注意：此字段可能返回 null，表示取不到有效值。
        :type IsSupportTDE: int
        :param DBEngine: 数据库引擎，支持：
1、postgresql（云数据库PostgreSQL）；
2、mssql_compatible（MSSQL兼容-云数据库PostgreSQL）；
注意：此字段可能返回 null，表示取不到有效值。
        :type DBEngine: str
        :param DBEngineConfig: 数据库引擎的配置信息
注意：此字段可能返回 null，表示取不到有效值。
        :type DBEngineConfig: str
        """
        self.Region = None
        self.Zone = None
        self.ProjectId = None
        self.VpcId = None
        self.SubnetId = None
        self.DBInstanceId = None
        self.DBInstanceName = None
        self.DBInstanceStatus = None
        self.DBInstanceMemory = None
        self.DBInstanceStorage = None
        self.DBInstanceCpu = None
        self.DBInstanceClass = None
        self.DBInstanceType = None
        self.DBInstanceVersion = None
        self.DBCharset = None
        self.DBVersion = None
        self.CreateTime = None
        self.UpdateTime = None
        self.ExpireTime = None
        self.IsolatedTime = None
        self.PayType = None
        self.AutoRenew = None
        self.DBInstanceNetInfo = None
        self.Type = None
        self.AppId = None
        self.Uid = None
        self.SupportIpv6 = None
        self.TagList = None
        self.MasterDBInstanceId = None
        self.ReadOnlyInstanceNum = None
        self.StatusInReadonlyGroup = None
        self.OfflineTime = None
        self.DBKernelVersion = None
        self.NetworkAccessList = None
        self.DBMajorVersion = None
        self.DBNodeSet = None
        self.IsSupportTDE = None
        self.DBEngine = None
        self.DBEngineConfig = None


    def _deserialize(self, params):
        self.Region = params.get("Region")
        self.Zone = params.get("Zone")
        self.ProjectId = params.get("ProjectId")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.DBInstanceId = params.get("DBInstanceId")
        self.DBInstanceName = params.get("DBInstanceName")
        self.DBInstanceStatus = params.get("DBInstanceStatus")
        self.DBInstanceMemory = params.get("DBInstanceMemory")
        self.DBInstanceStorage = params.get("DBInstanceStorage")
        self.DBInstanceCpu = params.get("DBInstanceCpu")
        self.DBInstanceClass = params.get("DBInstanceClass")
        self.DBInstanceType = params.get("DBInstanceType")
        self.DBInstanceVersion = params.get("DBInstanceVersion")
        self.DBCharset = params.get("DBCharset")
        self.DBVersion = params.get("DBVersion")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        self.ExpireTime = params.get("ExpireTime")
        self.IsolatedTime = params.get("IsolatedTime")
        self.PayType = params.get("PayType")
        self.AutoRenew = params.get("AutoRenew")
        if params.get("DBInstanceNetInfo") is not None:
            self.DBInstanceNetInfo = []
            for item in params.get("DBInstanceNetInfo"):
                obj = DBInstanceNetInfo()
                obj._deserialize(item)
                self.DBInstanceNetInfo.append(obj)
        self.Type = params.get("Type")
        self.AppId = params.get("AppId")
        self.Uid = params.get("Uid")
        self.SupportIpv6 = params.get("SupportIpv6")
        if params.get("TagList") is not None:
            self.TagList = []
            for item in params.get("TagList"):
                obj = Tag()
                obj._deserialize(item)
                self.TagList.append(obj)
        self.MasterDBInstanceId = params.get("MasterDBInstanceId")
        self.ReadOnlyInstanceNum = params.get("ReadOnlyInstanceNum")
        self.StatusInReadonlyGroup = params.get("StatusInReadonlyGroup")
        self.OfflineTime = params.get("OfflineTime")
        self.DBKernelVersion = params.get("DBKernelVersion")
        if params.get("NetworkAccessList") is not None:
            self.NetworkAccessList = []
            for item in params.get("NetworkAccessList"):
                obj = NetworkAccess()
                obj._deserialize(item)
                self.NetworkAccessList.append(obj)
        self.DBMajorVersion = params.get("DBMajorVersion")
        if params.get("DBNodeSet") is not None:
            self.DBNodeSet = []
            for item in params.get("DBNodeSet"):
                obj = DBNode()
                obj._deserialize(item)
                self.DBNodeSet.append(obj)
        self.IsSupportTDE = params.get("IsSupportTDE")
        self.DBEngine = params.get("DBEngine")
        self.DBEngineConfig = params.get("DBEngineConfig")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DBInstanceNetInfo(AbstractModel):
    """描述实例的网络连接信息。

    """

    def __init__(self):
        r"""
        :param Address: DNS域名
        :type Address: str
        :param Ip: IP地址
        :type Ip: str
        :param Port: 连接Port地址
        :type Port: int
        :param NetType: 网络类型，1、inner（基础网络内网地址）；2、private（私有网络内网地址）；3、public（基础网络或私有网络的外网地址）；
        :type NetType: str
        :param Status: 网络连接状态，1、initing（未开通）；2、opened（已开通）；3、closed（已关闭）；4、opening（开通中）；5、closing（关闭中）；
        :type Status: str
        :param VpcId: 私有网络ID
注意：此字段可能返回 null，表示取不到有效值。
        :type VpcId: str
        :param SubnetId: 子网ID
注意：此字段可能返回 null，表示取不到有效值。
        :type SubnetId: str
        :param ProtocolType: 连接数据库的协议类型，当前支持：postgresql、mssql（MSSQL兼容语法）
注意：此字段可能返回 null，表示取不到有效值。
        :type ProtocolType: str
        """
        self.Address = None
        self.Ip = None
        self.Port = None
        self.NetType = None
        self.Status = None
        self.VpcId = None
        self.SubnetId = None
        self.ProtocolType = None


    def _deserialize(self, params):
        self.Address = params.get("Address")
        self.Ip = params.get("Ip")
        self.Port = params.get("Port")
        self.NetType = params.get("NetType")
        self.Status = params.get("Status")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.ProtocolType = params.get("ProtocolType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DBNode(AbstractModel):
    """描述实例节点信息，包括节点类型、节点所在可用区。

    """

    def __init__(self):
        r"""
        :param Role: 节点类型，值可以为：
Primary，代表主节点；
Standby，代表备节点。
        :type Role: str
        :param Zone: 节点所在可用区，例如 ap-guangzhou-1。
        :type Zone: str
        """
        self.Role = None
        self.Zone = None


    def _deserialize(self, params):
        self.Role = params.get("Role")
        self.Zone = params.get("Zone")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteBaseBackupRequest(AbstractModel):
    """DeleteBaseBackup请求参数结构体

    """

    def __init__(self):
        r"""
        :param DBInstanceId: 实例ID。
        :type DBInstanceId: str
        :param BaseBackupId: 基础备份ID。
        :type BaseBackupId: str
        """
        self.DBInstanceId = None
        self.BaseBackupId = None


    def _deserialize(self, params):
        self.DBInstanceId = params.get("DBInstanceId")
        self.BaseBackupId = params.get("BaseBackupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteBaseBackupResponse(AbstractModel):
    """DeleteBaseBackup返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteDBInstanceNetworkAccessRequest(AbstractModel):
    """DeleteDBInstanceNetworkAccess请求参数结构体

    """

    def __init__(self):
        r"""
        :param DBInstanceId: 实例ID，形如：postgres-6bwgamo3。
        :type DBInstanceId: str
        :param VpcId: 私有网络统一 ID，若是基础网络则传"0"。
        :type VpcId: str
        :param SubnetId: 子网ID，若是基础网络则传"0"。
        :type SubnetId: str
        :param Vip: 目标VIP地址。
        :type Vip: str
        """
        self.DBInstanceId = None
        self.VpcId = None
        self.SubnetId = None
        self.Vip = None


    def _deserialize(self, params):
        self.DBInstanceId = params.get("DBInstanceId")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.Vip = params.get("Vip")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteDBInstanceNetworkAccessResponse(AbstractModel):
    """DeleteDBInstanceNetworkAccess返回参数结构体

    """

    def __init__(self):
        r"""
        :param FlowId: 流程ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type FlowId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.FlowId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        self.RequestId = params.get("RequestId")


class DeleteLogBackupRequest(AbstractModel):
    """DeleteLogBackup请求参数结构体

    """

    def __init__(self):
        r"""
        :param DBInstanceId: 实例ID。
        :type DBInstanceId: str
        :param LogBackupId: 日志备份ID。
        :type LogBackupId: str
        """
        self.DBInstanceId = None
        self.LogBackupId = None


    def _deserialize(self, params):
        self.DBInstanceId = params.get("DBInstanceId")
        self.LogBackupId = params.get("LogBackupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteLogBackupResponse(AbstractModel):
    """DeleteLogBackup返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteParameterTemplateRequest(AbstractModel):
    """DeleteParameterTemplate请求参数结构体

    """

    def __init__(self):
        r"""
        :param TemplateId: 参数模板ID，用于唯一确认待操作的参数模板
        :type TemplateId: str
        """
        self.TemplateId = None


    def _deserialize(self, params):
        self.TemplateId = params.get("TemplateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteParameterTemplateResponse(AbstractModel):
    """DeleteParameterTemplate返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteReadOnlyGroupNetworkAccessRequest(AbstractModel):
    """DeleteReadOnlyGroupNetworkAccess请求参数结构体

    """

    def __init__(self):
        r"""
        :param ReadOnlyGroupId: RO组ID，形如：pgro-4t9c6g7k。
        :type ReadOnlyGroupId: str
        :param VpcId: 私有网络统一 ID，若是基础网络则传"0"。
        :type VpcId: str
        :param SubnetId: 子网ID，若是基础网络则传"0"。
        :type SubnetId: str
        :param Vip: 目标VIP地址。
        :type Vip: str
        """
        self.ReadOnlyGroupId = None
        self.VpcId = None
        self.SubnetId = None
        self.Vip = None


    def _deserialize(self, params):
        self.ReadOnlyGroupId = params.get("ReadOnlyGroupId")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.Vip = params.get("Vip")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteReadOnlyGroupNetworkAccessResponse(AbstractModel):
    """DeleteReadOnlyGroupNetworkAccess返回参数结构体

    """

    def __init__(self):
        r"""
        :param FlowId: 流程ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type FlowId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.FlowId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        self.RequestId = params.get("RequestId")


class DeleteReadOnlyGroupRequest(AbstractModel):
    """DeleteReadOnlyGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param ReadOnlyGroupId: 待删除只读组ID
        :type ReadOnlyGroupId: str
        """
        self.ReadOnlyGroupId = None


    def _deserialize(self, params):
        self.ReadOnlyGroupId = params.get("ReadOnlyGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteReadOnlyGroupResponse(AbstractModel):
    """DeleteReadOnlyGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param FlowId: 流程ID
注意：此字段可能返回 null，表示取不到有效值。
        :type FlowId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.FlowId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        self.RequestId = params.get("RequestId")


class DeleteServerlessDBInstanceRequest(AbstractModel):
    """DeleteServerlessDBInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param DBInstanceName: DB实例名称，实例名和实例ID必须至少传一个，如果同时存在，将只以实例ID为准。
        :type DBInstanceName: str
        :param DBInstanceId: DB实例ID，实例名和实例ID必须至少传一个，如果同时存在，将只以实例ID为准。
        :type DBInstanceId: str
        """
        self.DBInstanceName = None
        self.DBInstanceId = None


    def _deserialize(self, params):
        self.DBInstanceName = params.get("DBInstanceName")
        self.DBInstanceId = params.get("DBInstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteServerlessDBInstanceResponse(AbstractModel):
    """DeleteServerlessDBInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeAccountsRequest(AbstractModel):
    """DescribeAccounts请求参数结构体

    """

    def __init__(self):
        r"""
        :param DBInstanceId: 实例ID，形如postgres-6fego161
        :type DBInstanceId: str
        :param Limit: 分页返回，每页最大返回数目，默认10，取值范围为1-100
        :type Limit: int
        :param Offset: 数据偏移量，从0开始。
        :type Offset: int
        :param OrderBy: 返回数据按照创建时间或者用户名排序。取值只能为createTime或者name。createTime-按照创建时间排序；name-按照用户名排序
        :type OrderBy: str
        :param OrderByType: 返回结果是升序还是降序。取值只能为desc或者asc。desc-降序；asc-升序
        :type OrderByType: str
        """
        self.DBInstanceId = None
        self.Limit = None
        self.Offset = None
        self.OrderBy = None
        self.OrderByType = None


    def _deserialize(self, params):
        self.DBInstanceId = params.get("DBInstanceId")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.OrderBy = params.get("OrderBy")
        self.OrderByType = params.get("OrderByType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAccountsResponse(AbstractModel):
    """DescribeAccounts返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 本次调用接口共返回了多少条数据。
        :type TotalCount: int
        :param Details: 帐号列表详细信息。
        :type Details: list of AccountInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Details = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Details") is not None:
            self.Details = []
            for item in params.get("Details"):
                obj = AccountInfo()
                obj._deserialize(item)
                self.Details.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeAvailableRecoveryTimeRequest(AbstractModel):
    """DescribeAvailableRecoveryTime请求参数结构体

    """

    def __init__(self):
        r"""
        :param DBInstanceId: 实例ID
        :type DBInstanceId: str
        """
        self.DBInstanceId = None


    def _deserialize(self, params):
        self.DBInstanceId = params.get("DBInstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAvailableRecoveryTimeResponse(AbstractModel):
    """DescribeAvailableRecoveryTime返回参数结构体

    """

    def __init__(self):
        r"""
        :param RecoveryBeginTime: 可恢复的最早时间，时区为东八区（UTC+8）。
        :type RecoveryBeginTime: str
        :param RecoveryEndTime: 可恢复的最晚时间，时区为东八区（UTC+8）。
        :type RecoveryEndTime: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RecoveryBeginTime = None
        self.RecoveryEndTime = None
        self.RequestId = None


    def _deserialize(self, params):
        self.RecoveryBeginTime = params.get("RecoveryBeginTime")
        self.RecoveryEndTime = params.get("RecoveryEndTime")
        self.RequestId = params.get("RequestId")


class DescribeBackupDownloadRestrictionRequest(AbstractModel):
    """DescribeBackupDownloadRestriction请求参数结构体

    """


class DescribeBackupDownloadRestrictionResponse(AbstractModel):
    """DescribeBackupDownloadRestriction返回参数结构体

    """

    def __init__(self):
        r"""
        :param RestrictionType: 备份文件下载限制类型，NONE 无限制，内外网都可以下载；INTRANET 只允许内网下载；CUSTOMIZE 自定义限制下载的vpc或ip。
        :type RestrictionType: str
        :param VpcRestrictionEffect: vpc限制效力，ALLOW 允许；DENY 拒绝。
注意：此字段可能返回 null，表示取不到有效值。
        :type VpcRestrictionEffect: str
        :param VpcIdSet: 允许或拒绝下载备份文件的vpcId列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type VpcIdSet: list of str
        :param IpRestrictionEffect: ip限制效力，ALLOW 允许；DENY 拒绝。
注意：此字段可能返回 null，表示取不到有效值。
        :type IpRestrictionEffect: str
        :param IpSet: 允许或拒绝下载备份文件的ip列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type IpSet: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RestrictionType = None
        self.VpcRestrictionEffect = None
        self.VpcIdSet = None
        self.IpRestrictionEffect = None
        self.IpSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.RestrictionType = params.get("RestrictionType")
        self.VpcRestrictionEffect = params.get("VpcRestrictionEffect")
        self.VpcIdSet = params.get("VpcIdSet")
        self.IpRestrictionEffect = params.get("IpRestrictionEffect")
        self.IpSet = params.get("IpSet")
        self.RequestId = params.get("RequestId")


class DescribeBackupDownloadURLRequest(AbstractModel):
    """DescribeBackupDownloadURL请求参数结构体

    """

    def __init__(self):
        r"""
        :param DBInstanceId: 实例ID。
        :type DBInstanceId: str
        :param BackupType: 备份类型，目前支持：LogBackup，BaseBackup。
        :type BackupType: str
        :param BackupId: 备份的唯一ID。
        :type BackupId: str
        :param URLExpireTime: 链接的有效时间，默认为12小时。
        :type URLExpireTime: int
        :param BackupDownloadRestriction: 备份下载限制
        :type BackupDownloadRestriction: :class:`tencentcloud.postgres.v20170312.models.BackupDownloadRestriction`
        """
        self.DBInstanceId = None
        self.BackupType = None
        self.BackupId = None
        self.URLExpireTime = None
        self.BackupDownloadRestriction = None


    def _deserialize(self, params):
        self.DBInstanceId = params.get("DBInstanceId")
        self.BackupType = params.get("BackupType")
        self.BackupId = params.get("BackupId")
        self.URLExpireTime = params.get("URLExpireTime")
        if params.get("BackupDownloadRestriction") is not None:
            self.BackupDownloadRestriction = BackupDownloadRestriction()
            self.BackupDownloadRestriction._deserialize(params.get("BackupDownloadRestriction"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBackupDownloadURLResponse(AbstractModel):
    """DescribeBackupDownloadURL返回参数结构体

    """

    def __init__(self):
        r"""
        :param BackupDownloadURL: 备份的下载地址。
        :type BackupDownloadURL: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.BackupDownloadURL = None
        self.RequestId = None


    def _deserialize(self, params):
        self.BackupDownloadURL = params.get("BackupDownloadURL")
        self.RequestId = params.get("RequestId")


class DescribeBackupOverviewRequest(AbstractModel):
    """DescribeBackupOverview请求参数结构体

    """


class DescribeBackupOverviewResponse(AbstractModel):
    """DescribeBackupOverview返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalFreeSize: 总免费空间大小，单位byte。
        :type TotalFreeSize: int
        :param UsedFreeSize: 已使用免费空间大小，单位byte。
        :type UsedFreeSize: int
        :param UsedBillingSize: 已使用收费空间大小，单位byte。
        :type UsedBillingSize: int
        :param LogBackupCount: 日志备份数量。
        :type LogBackupCount: int
        :param LogBackupSize: 日志备份大小，单位byte。
        :type LogBackupSize: int
        :param ManualBaseBackupCount: 手动创建的基础备份数量。
        :type ManualBaseBackupCount: int
        :param ManualBaseBackupSize: 手动创建的基础备份大小，单位byte。
        :type ManualBaseBackupSize: int
        :param AutoBaseBackupCount: 自动创建的基础备份数量。
        :type AutoBaseBackupCount: int
        :param AutoBaseBackupSize: 自动创建的基础备份大小，单位byte。
        :type AutoBaseBackupSize: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalFreeSize = None
        self.UsedFreeSize = None
        self.UsedBillingSize = None
        self.LogBackupCount = None
        self.LogBackupSize = None
        self.ManualBaseBackupCount = None
        self.ManualBaseBackupSize = None
        self.AutoBaseBackupCount = None
        self.AutoBaseBackupSize = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalFreeSize = params.get("TotalFreeSize")
        self.UsedFreeSize = params.get("UsedFreeSize")
        self.UsedBillingSize = params.get("UsedBillingSize")
        self.LogBackupCount = params.get("LogBackupCount")
        self.LogBackupSize = params.get("LogBackupSize")
        self.ManualBaseBackupCount = params.get("ManualBaseBackupCount")
        self.ManualBaseBackupSize = params.get("ManualBaseBackupSize")
        self.AutoBaseBackupCount = params.get("AutoBaseBackupCount")
        self.AutoBaseBackupSize = params.get("AutoBaseBackupSize")
        self.RequestId = params.get("RequestId")


class DescribeBackupPlansRequest(AbstractModel):
    """DescribeBackupPlans请求参数结构体

    """

    def __init__(self):
        r"""
        :param DBInstanceId: 实例ID
        :type DBInstanceId: str
        """
        self.DBInstanceId = None


    def _deserialize(self, params):
        self.DBInstanceId = params.get("DBInstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBackupPlansResponse(AbstractModel):
    """DescribeBackupPlans返回参数结构体

    """

    def __init__(self):
        r"""
        :param Plans: 实例的备份计划集
        :type Plans: list of BackupPlan
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Plans = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Plans") is not None:
            self.Plans = []
            for item in params.get("Plans"):
                obj = BackupPlan()
                obj._deserialize(item)
                self.Plans.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeBackupSummariesRequest(AbstractModel):
    """DescribeBackupSummaries请求参数结构体

    """

    def __init__(self):
        r"""
        :param Limit: 每页显示数量，取值范围为1-100，默认为返回10条。
        :type Limit: int
        :param Offset: 数据偏移量，从0开始。
        :type Offset: int
        :param Filters: 按照一个或者多个过滤条件进行查询，目前支持的过滤条件有：
db-instance-id：按照实例ID过滤，类型为string。
db-instance-name：按照实例名过滤，类型为string。
db-instance-ip：按照实例私有网络IP地址过滤，类型为string。
        :type Filters: list of Filter
        :param OrderBy: 排序字段，支持TotalBackupSize,LogBackupSize,ManualBaseBackupSize,AutoBaseBackupSize。
        :type OrderBy: str
        :param OrderByType: 排序方式，包括升序：asc，降序：desc。
        :type OrderByType: str
        """
        self.Limit = None
        self.Offset = None
        self.Filters = None
        self.OrderBy = None
        self.OrderByType = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.OrderBy = params.get("OrderBy")
        self.OrderByType = params.get("OrderByType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBackupSummariesResponse(AbstractModel):
    """DescribeBackupSummaries返回参数结构体

    """

    def __init__(self):
        r"""
        :param BackupSummarySet: 备份统计信息列表。
        :type BackupSummarySet: list of BackupSummary
        :param TotalCount: 查询到的所有备份信息数量。
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.BackupSummarySet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("BackupSummarySet") is not None:
            self.BackupSummarySet = []
            for item in params.get("BackupSummarySet"):
                obj = BackupSummary()
                obj._deserialize(item)
                self.BackupSummarySet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeBaseBackupsRequest(AbstractModel):
    """DescribeBaseBackups请求参数结构体

    """

    def __init__(self):
        r"""
        :param MinFinishTime: 备份的最小结束时间，形如2018-01-01 00:00:00。默认为7天前。
        :type MinFinishTime: str
        :param MaxFinishTime: 备份的最大结束时间，形如2018-01-01 00:00:00。默认为当前时间。
        :type MaxFinishTime: str
        :param Filters: 按照一个或者多个过滤条件进行查询，目前支持的过滤条件有：
db-instance-id：按照实例ID过滤，类型为string。
db-instance-name：按照实例名过滤，类型为string。
db-instance-ip：按照实例私有网络IP地址过滤，类型为string。
        :type Filters: list of Filter
        :param Limit: 每页显示数量，取值范围为1-100，默认为返回10条。
        :type Limit: int
        :param Offset: 数据偏移量，从0开始。
        :type Offset: int
        :param OrderBy: 排序字段，支持StartTime,FinishTime,Size。
        :type OrderBy: str
        :param OrderByType: 排序方式，包括升序：asc，降序：desc。
        :type OrderByType: str
        """
        self.MinFinishTime = None
        self.MaxFinishTime = None
        self.Filters = None
        self.Limit = None
        self.Offset = None
        self.OrderBy = None
        self.OrderByType = None


    def _deserialize(self, params):
        self.MinFinishTime = params.get("MinFinishTime")
        self.MaxFinishTime = params.get("MaxFinishTime")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.OrderBy = params.get("OrderBy")
        self.OrderByType = params.get("OrderByType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBaseBackupsResponse(AbstractModel):
    """DescribeBaseBackups返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 查询到的基础备份数量。
        :type TotalCount: int
        :param BaseBackupSet: 基础备份详细信息列表。
        :type BaseBackupSet: list of BaseBackup
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.BaseBackupSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("BaseBackupSet") is not None:
            self.BaseBackupSet = []
            for item in params.get("BaseBackupSet"):
                obj = BaseBackup()
                obj._deserialize(item)
                self.BaseBackupSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeClassesRequest(AbstractModel):
    """DescribeClasses请求参数结构体

    """

    def __init__(self):
        r"""
        :param Zone: 可用区ID。可以通过接口DescribeZones获取。
        :type Zone: str
        :param DBEngine: 数据库引擎，支持：
1、postgresql（云数据库PostgreSQL）；
2、mssql_compatible（MSSQL兼容-云数据库PostgreSQL）；
        :type DBEngine: str
        :param DBMajorVersion: 数据库主版本号。例如12，13，可以通过接口DescribeDBVersions获取。
        :type DBMajorVersion: str
        """
        self.Zone = None
        self.DBEngine = None
        self.DBMajorVersion = None


    def _deserialize(self, params):
        self.Zone = params.get("Zone")
        self.DBEngine = params.get("DBEngine")
        self.DBMajorVersion = params.get("DBMajorVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeClassesResponse(AbstractModel):
    """DescribeClasses返回参数结构体

    """

    def __init__(self):
        r"""
        :param ClassInfoSet: 数据库规格列表
        :type ClassInfoSet: list of ClassInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ClassInfoSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ClassInfoSet") is not None:
            self.ClassInfoSet = []
            for item in params.get("ClassInfoSet"):
                obj = ClassInfo()
                obj._deserialize(item)
                self.ClassInfoSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeCloneDBInstanceSpecRequest(AbstractModel):
    """DescribeCloneDBInstanceSpec请求参数结构体

    """

    def __init__(self):
        r"""
        :param DBInstanceId: 实例ID。
        :type DBInstanceId: str
        :param BackupSetId: 基础备份集ID，此入参和RecoveryTargetTime必须选择一个传入。如与RecoveryTargetTime参数同时设置，则以此参数为准。
        :type BackupSetId: str
        :param RecoveryTargetTime: 恢复目标时间，此入参和BackupSetId必须选择一个传入。时区以东八区（UTC+8）为准。
        :type RecoveryTargetTime: str
        """
        self.DBInstanceId = None
        self.BackupSetId = None
        self.RecoveryTargetTime = None


    def _deserialize(self, params):
        self.DBInstanceId = params.get("DBInstanceId")
        self.BackupSetId = params.get("BackupSetId")
        self.RecoveryTargetTime = params.get("RecoveryTargetTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCloneDBInstanceSpecResponse(AbstractModel):
    """DescribeCloneDBInstanceSpec返回参数结构体

    """

    def __init__(self):
        r"""
        :param MinSpecCode: 可购买的最小规格码。
        :type MinSpecCode: str
        :param MinStorage: 可购买的最小磁盘容量，单位GB。
        :type MinStorage: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.MinSpecCode = None
        self.MinStorage = None
        self.RequestId = None


    def _deserialize(self, params):
        self.MinSpecCode = params.get("MinSpecCode")
        self.MinStorage = params.get("MinStorage")
        self.RequestId = params.get("RequestId")


class DescribeDBBackupsRequest(AbstractModel):
    """DescribeDBBackups请求参数结构体

    """

    def __init__(self):
        r"""
        :param DBInstanceId: 实例ID，形如postgres-4wdeb0zv。
        :type DBInstanceId: str
        :param Type: 备份方式（1-全量）。目前只支持全量，取值为1。
        :type Type: int
        :param StartTime: 查询开始时间，形如2018-06-10 17:06:38，起始时间不得小于7天以前
        :type StartTime: str
        :param EndTime: 查询结束时间，形如2018-06-10 17:06:38
        :type EndTime: str
        :param Limit: 备份列表分页返回，每页返回数量，默认为 20，最小为1，最大值为 100。（当该参数不传或者传0时按默认值处理）
        :type Limit: int
        :param Offset: 返回结果中的第几页，从第0页开始。默认为0。
        :type Offset: int
        """
        self.DBInstanceId = None
        self.Type = None
        self.StartTime = None
        self.EndTime = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.DBInstanceId = params.get("DBInstanceId")
        self.Type = params.get("Type")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDBBackupsResponse(AbstractModel):
    """DescribeDBBackups返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 返回备份列表中备份文件的个数
        :type TotalCount: int
        :param BackupList: 备份列表
        :type BackupList: list of DBBackup
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.BackupList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("BackupList") is not None:
            self.BackupList = []
            for item in params.get("BackupList"):
                obj = DBBackup()
                obj._deserialize(item)
                self.BackupList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDBErrlogsRequest(AbstractModel):
    """DescribeDBErrlogs请求参数结构体

    """

    def __init__(self):
        r"""
        :param DBInstanceId: 实例ID，形如postgres-5bq3wfjd
        :type DBInstanceId: str
        :param StartTime: 查询起始时间，形如2018-01-01 00:00:00，起始时间不得小于7天以前
        :type StartTime: str
        :param EndTime: 查询结束时间，形如2018-01-01 00:00:00
        :type EndTime: str
        :param DatabaseName: 数据库名字
        :type DatabaseName: str
        :param SearchKeys: 搜索关键字
        :type SearchKeys: list of str
        :param Limit: 分页返回，每页返回的最大数量。取值为1-100
        :type Limit: int
        :param Offset: 分页返回，返回第几页的数据，从第0页开始计数
        :type Offset: int
        """
        self.DBInstanceId = None
        self.StartTime = None
        self.EndTime = None
        self.DatabaseName = None
        self.SearchKeys = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.DBInstanceId = params.get("DBInstanceId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.DatabaseName = params.get("DatabaseName")
        self.SearchKeys = params.get("SearchKeys")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDBErrlogsResponse(AbstractModel):
    """DescribeDBErrlogs返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 本次调用返回了多少条数据
        :type TotalCount: int
        :param Details: 错误日志列表
        :type Details: list of ErrLogDetail
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Details = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Details") is not None:
            self.Details = []
            for item in params.get("Details"):
                obj = ErrLogDetail()
                obj._deserialize(item)
                self.Details.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDBInstanceAttributeRequest(AbstractModel):
    """DescribeDBInstanceAttribute请求参数结构体

    """

    def __init__(self):
        r"""
        :param DBInstanceId: 实例ID
        :type DBInstanceId: str
        """
        self.DBInstanceId = None


    def _deserialize(self, params):
        self.DBInstanceId = params.get("DBInstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDBInstanceAttributeResponse(AbstractModel):
    """DescribeDBInstanceAttribute返回参数结构体

    """

    def __init__(self):
        r"""
        :param DBInstance: 实例详细信息。
        :type DBInstance: :class:`tencentcloud.postgres.v20170312.models.DBInstance`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DBInstance = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DBInstance") is not None:
            self.DBInstance = DBInstance()
            self.DBInstance._deserialize(params.get("DBInstance"))
        self.RequestId = params.get("RequestId")


class DescribeDBInstanceParametersRequest(AbstractModel):
    """DescribeDBInstanceParameters请求参数结构体

    """

    def __init__(self):
        r"""
        :param DBInstanceId: 实例ID
        :type DBInstanceId: str
        :param ParamName: 查询指定参数详情。ParamName为空或不传，默认返回全部参数列表
        :type ParamName: str
        """
        self.DBInstanceId = None
        self.ParamName = None


    def _deserialize(self, params):
        self.DBInstanceId = params.get("DBInstanceId")
        self.ParamName = params.get("ParamName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDBInstanceParametersResponse(AbstractModel):
    """DescribeDBInstanceParameters返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 参数列表总数
        :type TotalCount: int
        :param Detail: 参数列表返回详情
        :type Detail: list of ParamInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Detail = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Detail") is not None:
            self.Detail = []
            for item in params.get("Detail"):
                obj = ParamInfo()
                obj._deserialize(item)
                self.Detail.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDBInstanceSecurityGroupsRequest(AbstractModel):
    """DescribeDBInstanceSecurityGroups请求参数结构体

    """

    def __init__(self):
        r"""
        :param DBInstanceId: 实例ID，DBInstanceId和ReadOnlyGroupId至少传一个；如果都传，忽略ReadOnlyGroupId
        :type DBInstanceId: str
        :param ReadOnlyGroupId: 只读组ID，DBInstanceId和ReadOnlyGroupId至少传一个；如果要查询只读组关联的安全组，只传ReadOnlyGroupId
        :type ReadOnlyGroupId: str
        """
        self.DBInstanceId = None
        self.ReadOnlyGroupId = None


    def _deserialize(self, params):
        self.DBInstanceId = params.get("DBInstanceId")
        self.ReadOnlyGroupId = params.get("ReadOnlyGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDBInstanceSecurityGroupsResponse(AbstractModel):
    """DescribeDBInstanceSecurityGroups返回参数结构体

    """

    def __init__(self):
        r"""
        :param SecurityGroupSet: 安全组信息数组
        :type SecurityGroupSet: list of SecurityGroup
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.SecurityGroupSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("SecurityGroupSet") is not None:
            self.SecurityGroupSet = []
            for item in params.get("SecurityGroupSet"):
                obj = SecurityGroup()
                obj._deserialize(item)
                self.SecurityGroupSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDBInstancesRequest(AbstractModel):
    """DescribeDBInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param Filters: 按照一个或者多个过滤条件进行查询，目前支持的过滤条件有：
db-instance-id：按照实例ID过滤，类型为string
db-instance-name：按照实例名过滤，类型为string
db-project-id：按照项目ID过滤，类型为integer
db-pay-mode：按照付费模式过滤，类型为string
db-tag-key：按照标签键过滤，类型为string
        :type Filters: list of Filter
        :param Limit: 每页显示数量，取值范围为1-100，默认为返回10条。
        :type Limit: int
        :param Offset: 数据偏移量，从0开始。
        :type Offset: int
        :param OrderBy: 排序指标，如实例名、创建时间等，支持DBInstanceId,CreateTime,Name,EndTime
        :type OrderBy: str
        :param OrderByType: 排序方式，包括升序：asc、降序：desc。
        :type OrderByType: str
        """
        self.Filters = None
        self.Limit = None
        self.Offset = None
        self.OrderBy = None
        self.OrderByType = None


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.OrderBy = params.get("OrderBy")
        self.OrderByType = params.get("OrderByType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDBInstancesResponse(AbstractModel):
    """DescribeDBInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 查询到的实例数量。
        :type TotalCount: int
        :param DBInstanceSet: 实例详细信息集合。
        :type DBInstanceSet: list of DBInstance
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.DBInstanceSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("DBInstanceSet") is not None:
            self.DBInstanceSet = []
            for item in params.get("DBInstanceSet"):
                obj = DBInstance()
                obj._deserialize(item)
                self.DBInstanceSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDBSlowlogsRequest(AbstractModel):
    """DescribeDBSlowlogs请求参数结构体

    """

    def __init__(self):
        r"""
        :param DBInstanceId: 实例ID，形如postgres-lnp6j617
        :type DBInstanceId: str
        :param StartTime: 查询起始时间，形如2018-06-10 17:06:38，起始时间不得小于7天以前
        :type StartTime: str
        :param EndTime: 查询结束时间，形如2018-06-10 17:06:38
        :type EndTime: str
        :param DatabaseName: 数据库名字
        :type DatabaseName: str
        :param OrderBy: 按照何种指标排序，取值为sum_calls或者sum_cost_time。sum_calls-总调用次数；sum_cost_time-总的花费时间
        :type OrderBy: str
        :param OrderByType: 排序规则。desc-降序；asc-升序
        :type OrderByType: str
        :param Limit: 分页返回结果，每页最大返回数量，取值为1-100，默认20
        :type Limit: int
        :param Offset: 分页返回结果，返回结果的第几页，从0开始计数
        :type Offset: int
        """
        self.DBInstanceId = None
        self.StartTime = None
        self.EndTime = None
        self.DatabaseName = None
        self.OrderBy = None
        self.OrderByType = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.DBInstanceId = params.get("DBInstanceId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.DatabaseName = params.get("DatabaseName")
        self.OrderBy = params.get("OrderBy")
        self.OrderByType = params.get("OrderByType")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDBSlowlogsResponse(AbstractModel):
    """DescribeDBSlowlogs返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 本次返回多少条数据
        :type TotalCount: int
        :param Detail: 慢查询日志详情
        :type Detail: :class:`tencentcloud.postgres.v20170312.models.SlowlogDetail`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Detail = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Detail") is not None:
            self.Detail = SlowlogDetail()
            self.Detail._deserialize(params.get("Detail"))
        self.RequestId = params.get("RequestId")


class DescribeDBVersionsRequest(AbstractModel):
    """DescribeDBVersions请求参数结构体

    """


class DescribeDBVersionsResponse(AbstractModel):
    """DescribeDBVersions返回参数结构体

    """

    def __init__(self):
        r"""
        :param VersionSet: 数据库版本号信息列表
        :type VersionSet: list of Version
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.VersionSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("VersionSet") is not None:
            self.VersionSet = []
            for item in params.get("VersionSet"):
                obj = Version()
                obj._deserialize(item)
                self.VersionSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDBXlogsRequest(AbstractModel):
    """DescribeDBXlogs请求参数结构体

    """

    def __init__(self):
        r"""
        :param DBInstanceId: 实例ID，形如postgres-4wdeb0zv。
        :type DBInstanceId: str
        :param StartTime: 查询开始时间，形如2018-06-10 17:06:38，起始时间不得小于7天以前
        :type StartTime: str
        :param EndTime: 查询结束时间，形如2018-06-10 17:06:38
        :type EndTime: str
        :param Offset: 分页返回，表示返回第几页的条目。从第0页开始计数。
        :type Offset: int
        :param Limit: 分页返回，表示每页有多少条目。取值为1-100。
        :type Limit: int
        """
        self.DBInstanceId = None
        self.StartTime = None
        self.EndTime = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.DBInstanceId = params.get("DBInstanceId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDBXlogsResponse(AbstractModel):
    """DescribeDBXlogs返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 表示此次返回结果有多少条数据。
        :type TotalCount: int
        :param XlogList: Xlog列表
        :type XlogList: list of Xlog
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.XlogList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("XlogList") is not None:
            self.XlogList = []
            for item in params.get("XlogList"):
                obj = Xlog()
                obj._deserialize(item)
                self.XlogList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDatabasesRequest(AbstractModel):
    """DescribeDatabases请求参数结构体

    """

    def __init__(self):
        r"""
        :param DBInstanceId: 实例ID
        :type DBInstanceId: str
        """
        self.DBInstanceId = None


    def _deserialize(self, params):
        self.DBInstanceId = params.get("DBInstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDatabasesResponse(AbstractModel):
    """DescribeDatabases返回参数结构体

    """

    def __init__(self):
        r"""
        :param Items: 数据库信息
        :type Items: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Items = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Items = params.get("Items")
        self.RequestId = params.get("RequestId")


class DescribeDefaultParametersRequest(AbstractModel):
    """DescribeDefaultParameters请求参数结构体

    """

    def __init__(self):
        r"""
        :param DBMajorVersion: 数据库版本，大版本号，例如11，12，13
        :type DBMajorVersion: str
        :param DBEngine: 数据库引擎，例如：postgresql,mssql_compatible
        :type DBEngine: str
        """
        self.DBMajorVersion = None
        self.DBEngine = None


    def _deserialize(self, params):
        self.DBMajorVersion = params.get("DBMajorVersion")
        self.DBEngine = params.get("DBEngine")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDefaultParametersResponse(AbstractModel):
    """DescribeDefaultParameters返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 参数个数
        :type TotalCount: int
        :param ParamInfoSet: 参数信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ParamInfoSet: list of ParamInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.ParamInfoSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("ParamInfoSet") is not None:
            self.ParamInfoSet = []
            for item in params.get("ParamInfoSet"):
                obj = ParamInfo()
                obj._deserialize(item)
                self.ParamInfoSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeEncryptionKeysRequest(AbstractModel):
    """DescribeEncryptionKeys请求参数结构体

    """

    def __init__(self):
        r"""
        :param DBInstanceId: 实例ID。
        :type DBInstanceId: str
        """
        self.DBInstanceId = None


    def _deserialize(self, params):
        self.DBInstanceId = params.get("DBInstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeEncryptionKeysResponse(AbstractModel):
    """DescribeEncryptionKeys返回参数结构体

    """

    def __init__(self):
        r"""
        :param EncryptionKeys: 实例密钥信息列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type EncryptionKeys: list of EncryptionKey
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.EncryptionKeys = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("EncryptionKeys") is not None:
            self.EncryptionKeys = []
            for item in params.get("EncryptionKeys"):
                obj = EncryptionKey()
                obj._deserialize(item)
                self.EncryptionKeys.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeLogBackupsRequest(AbstractModel):
    """DescribeLogBackups请求参数结构体

    """

    def __init__(self):
        r"""
        :param MinFinishTime: 备份的最小结束时间，形如2018-01-01 00:00:00。默认为7天前。
        :type MinFinishTime: str
        :param MaxFinishTime: 备份的最大结束时间，形如2018-01-01 00:00:00。默认为当前时间。
        :type MaxFinishTime: str
        :param Filters: 按照一个或者多个过滤条件进行查询，目前支持的过滤条件有：
db-instance-id：按照实例ID过滤，类型为string。
db-instance-name：按照实例名过滤，类型为string。
db-instance-ip：按照实例私有网络IP地址过滤，类型为string。
        :type Filters: list of Filter
        :param Limit: 每页显示数量，取值范围为1-100，默认为返回10条。
        :type Limit: int
        :param Offset: 数据偏移量，从0开始。
        :type Offset: int
        :param OrderBy: 排序字段，支持StartTime,FinishTime,Size。
        :type OrderBy: str
        :param OrderByType: 排序方式，包括升序：asc，降序：desc。
        :type OrderByType: str
        """
        self.MinFinishTime = None
        self.MaxFinishTime = None
        self.Filters = None
        self.Limit = None
        self.Offset = None
        self.OrderBy = None
        self.OrderByType = None


    def _deserialize(self, params):
        self.MinFinishTime = params.get("MinFinishTime")
        self.MaxFinishTime = params.get("MaxFinishTime")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.OrderBy = params.get("OrderBy")
        self.OrderByType = params.get("OrderByType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLogBackupsResponse(AbstractModel):
    """DescribeLogBackups返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 查询到的日志备份数量。
        :type TotalCount: int
        :param LogBackupSet: 日志备份详细信息列表。
        :type LogBackupSet: list of LogBackup
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.LogBackupSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("LogBackupSet") is not None:
            self.LogBackupSet = []
            for item in params.get("LogBackupSet"):
                obj = LogBackup()
                obj._deserialize(item)
                self.LogBackupSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeOrdersRequest(AbstractModel):
    """DescribeOrders请求参数结构体

    """

    def __init__(self):
        r"""
        :param DealNames: 订单名集合
        :type DealNames: list of str
        """
        self.DealNames = None


    def _deserialize(self, params):
        self.DealNames = params.get("DealNames")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeOrdersResponse(AbstractModel):
    """DescribeOrders返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 订单数量
        :type TotalCount: int
        :param Deals: 订单数组
        :type Deals: list of PgDeal
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Deals = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Deals") is not None:
            self.Deals = []
            for item in params.get("Deals"):
                obj = PgDeal()
                obj._deserialize(item)
                self.Deals.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeParameterTemplateAttributesRequest(AbstractModel):
    """DescribeParameterTemplateAttributes请求参数结构体

    """

    def __init__(self):
        r"""
        :param TemplateId: 参数模板ID
        :type TemplateId: str
        """
        self.TemplateId = None


    def _deserialize(self, params):
        self.TemplateId = params.get("TemplateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeParameterTemplateAttributesResponse(AbstractModel):
    """DescribeParameterTemplateAttributes返回参数结构体

    """

    def __init__(self):
        r"""
        :param TemplateId: 参数模板ID
注意：此字段可能返回 null，表示取不到有效值。
        :type TemplateId: str
        :param TotalCount: 参数模板包含的参数个数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param ParamInfoSet: 参数模板包含的参数信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ParamInfoSet: list of ParamInfo
        :param TemplateName: 参数模板名称
注意：此字段可能返回 null，表示取不到有效值。
        :type TemplateName: str
        :param DBMajorVersion: 参数模板适用的数据库版本
注意：此字段可能返回 null，表示取不到有效值。
        :type DBMajorVersion: str
        :param DBEngine: 参数模板适用的数据库引擎
注意：此字段可能返回 null，表示取不到有效值。
        :type DBEngine: str
        :param TemplateDescription: 参数模板描述
注意：此字段可能返回 null，表示取不到有效值。
        :type TemplateDescription: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TemplateId = None
        self.TotalCount = None
        self.ParamInfoSet = None
        self.TemplateName = None
        self.DBMajorVersion = None
        self.DBEngine = None
        self.TemplateDescription = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TemplateId = params.get("TemplateId")
        self.TotalCount = params.get("TotalCount")
        if params.get("ParamInfoSet") is not None:
            self.ParamInfoSet = []
            for item in params.get("ParamInfoSet"):
                obj = ParamInfo()
                obj._deserialize(item)
                self.ParamInfoSet.append(obj)
        self.TemplateName = params.get("TemplateName")
        self.DBMajorVersion = params.get("DBMajorVersion")
        self.DBEngine = params.get("DBEngine")
        self.TemplateDescription = params.get("TemplateDescription")
        self.RequestId = params.get("RequestId")


class DescribeParameterTemplatesRequest(AbstractModel):
    """DescribeParameterTemplates请求参数结构体

    """

    def __init__(self):
        r"""
        :param Filters: 过滤条件，目前支持的过滤条件有：TemplateName, TemplateId，DBMajorVersion，DBEngine
        :type Filters: list of Filter
        :param Limit: 每页显示数量，[0，100]，默认 20
        :type Limit: int
        :param Offset: 数据偏移量
        :type Offset: int
        :param OrderBy: 排序指标，枚举值，支持：CreateTime，TemplateName，DBMajorVersion
        :type OrderBy: str
        :param OrderByType: 排序方式，枚举值，支持：asc（升序） ，desc（降序）
        :type OrderByType: str
        """
        self.Filters = None
        self.Limit = None
        self.Offset = None
        self.OrderBy = None
        self.OrderByType = None


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.OrderBy = params.get("OrderBy")
        self.OrderByType = params.get("OrderByType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeParameterTemplatesResponse(AbstractModel):
    """DescribeParameterTemplates返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 符合查询条件的参数模板总数
        :type TotalCount: int
        :param ParameterTemplateSet: 参数模板列表
        :type ParameterTemplateSet: list of ParameterTemplate
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.ParameterTemplateSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("ParameterTemplateSet") is not None:
            self.ParameterTemplateSet = []
            for item in params.get("ParameterTemplateSet"):
                obj = ParameterTemplate()
                obj._deserialize(item)
                self.ParameterTemplateSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeParamsEventRequest(AbstractModel):
    """DescribeParamsEvent请求参数结构体

    """

    def __init__(self):
        r"""
        :param DBInstanceId: 实例DB ID
        :type DBInstanceId: str
        """
        self.DBInstanceId = None


    def _deserialize(self, params):
        self.DBInstanceId = params.get("DBInstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeParamsEventResponse(AbstractModel):
    """DescribeParamsEvent返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 参数修改事件总数，以参数为统计粒度
        :type TotalCount: int
        :param EventItems: 实例参数修改事件详情
        :type EventItems: list of EventItem
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.EventItems = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("EventItems") is not None:
            self.EventItems = []
            for item in params.get("EventItems"):
                obj = EventItem()
                obj._deserialize(item)
                self.EventItems.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeProductConfigRequest(AbstractModel):
    """DescribeProductConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param Zone: 可用区名称
        :type Zone: str
        :param DBEngine: 数据库引擎，支持：
1、postgresql（云数据库PostgreSQL）；
2、mssql_compatible（MSSQL兼容-云数据库PostgreSQL）；
如不指定默认使用postgresql。
        :type DBEngine: str
        """
        self.Zone = None
        self.DBEngine = None


    def _deserialize(self, params):
        self.Zone = params.get("Zone")
        self.DBEngine = params.get("DBEngine")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeProductConfigResponse(AbstractModel):
    """DescribeProductConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param SpecInfoList: 售卖规格列表。
        :type SpecInfoList: list of SpecInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.SpecInfoList = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("SpecInfoList") is not None:
            self.SpecInfoList = []
            for item in params.get("SpecInfoList"):
                obj = SpecInfo()
                obj._deserialize(item)
                self.SpecInfoList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeReadOnlyGroupsRequest(AbstractModel):
    """DescribeReadOnlyGroups请求参数结构体

    """

    def __init__(self):
        r"""
        :param Filters: 过滤条件，必须传入主实例ID进行过滤，否则返回值将为空，过滤参数为：db-master-instance-id
        :type Filters: list of Filter
        :param PageSize: 查询每一页的条数，默认为10
        :type PageSize: int
        :param PageNumber: 查询的页码，默认为1
        :type PageNumber: int
        :param OrderBy: 查询排序依据，目前支持:ROGroupId,CreateTime,Name
        :type OrderBy: str
        :param OrderByType: 查询排序依据类型，目前支持:desc,asc
        :type OrderByType: str
        """
        self.Filters = None
        self.PageSize = None
        self.PageNumber = None
        self.OrderBy = None
        self.OrderByType = None


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.PageSize = params.get("PageSize")
        self.PageNumber = params.get("PageNumber")
        self.OrderBy = params.get("OrderBy")
        self.OrderByType = params.get("OrderByType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeReadOnlyGroupsResponse(AbstractModel):
    """DescribeReadOnlyGroups返回参数结构体

    """

    def __init__(self):
        r"""
        :param ReadOnlyGroupList: 只读组列表
        :type ReadOnlyGroupList: list of ReadOnlyGroup
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ReadOnlyGroupList = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ReadOnlyGroupList") is not None:
            self.ReadOnlyGroupList = []
            for item in params.get("ReadOnlyGroupList"):
                obj = ReadOnlyGroup()
                obj._deserialize(item)
                self.ReadOnlyGroupList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeRegionsRequest(AbstractModel):
    """DescribeRegions请求参数结构体

    """


class DescribeRegionsResponse(AbstractModel):
    """DescribeRegions返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 返回的结果数量。
        :type TotalCount: int
        :param RegionSet: 地域信息集合。
        :type RegionSet: list of RegionInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.RegionSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("RegionSet") is not None:
            self.RegionSet = []
            for item in params.get("RegionSet"):
                obj = RegionInfo()
                obj._deserialize(item)
                self.RegionSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeServerlessDBInstancesRequest(AbstractModel):
    """DescribeServerlessDBInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param Filter: 查询条件
        :type Filter: list of Filter
        :param Limit: 查询个数
        :type Limit: int
        :param Offset: 偏移量
        :type Offset: int
        :param OrderBy: 排序指标，目前支持实例创建时间CreateTime
        :type OrderBy: str
        :param OrderByType: 排序方式，包括升序、降序
        :type OrderByType: str
        """
        self.Filter = None
        self.Limit = None
        self.Offset = None
        self.OrderBy = None
        self.OrderByType = None


    def _deserialize(self, params):
        if params.get("Filter") is not None:
            self.Filter = []
            for item in params.get("Filter"):
                obj = Filter()
                obj._deserialize(item)
                self.Filter.append(obj)
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.OrderBy = params.get("OrderBy")
        self.OrderByType = params.get("OrderByType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeServerlessDBInstancesResponse(AbstractModel):
    """DescribeServerlessDBInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 查询结果数
        :type TotalCount: int
        :param DBInstanceSet: 查询结果
注意：此字段可能返回 null，表示取不到有效值。
        :type DBInstanceSet: list of ServerlessDBInstance
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.DBInstanceSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("DBInstanceSet") is not None:
            self.DBInstanceSet = []
            for item in params.get("DBInstanceSet"):
                obj = ServerlessDBInstance()
                obj._deserialize(item)
                self.DBInstanceSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeSlowQueryAnalysisRequest(AbstractModel):
    """DescribeSlowQueryAnalysis请求参数结构体

    """

    def __init__(self):
        r"""
        :param DBInstanceId: 实例ID。
        :type DBInstanceId: str
        :param StartTime: 查询起始时间戳，格式 “YYYY-MM-DD HH:mm:ss” ，日志保留时间默认为7天，起始时间不能超出保留时间范围。
        :type StartTime: str
        :param EndTime: 查询结束时间戳，格式 “YYYY-MM-DD HH:mm:ss”。
        :type EndTime: str
        :param DatabaseName: 根据数据库名进行筛选，可以为空。
        :type DatabaseName: str
        :param OrderBy: 排序维度。 可选参数，取值范围[CallNum,CostTime,AvgCostTime]。默认CallNum。
        :type OrderBy: str
        :param OrderByType: 排序类型。升序asc、降序desc。默认desc。
        :type OrderByType: str
        :param Limit: 分页大小。取值范围[1,100]。默认50。
        :type Limit: int
        :param Offset: 分页偏移。取值范围[0,INF)。默认0。
        :type Offset: int
        """
        self.DBInstanceId = None
        self.StartTime = None
        self.EndTime = None
        self.DatabaseName = None
        self.OrderBy = None
        self.OrderByType = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.DBInstanceId = params.get("DBInstanceId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.DatabaseName = params.get("DatabaseName")
        self.OrderBy = params.get("OrderBy")
        self.OrderByType = params.get("OrderByType")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSlowQueryAnalysisResponse(AbstractModel):
    """DescribeSlowQueryAnalysis返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 查询总条数。
        :type TotalCount: int
        :param Detail: 慢SQL统计分析接口返回详情。
        :type Detail: :class:`tencentcloud.postgres.v20170312.models.Detail`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Detail = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Detail") is not None:
            self.Detail = Detail()
            self.Detail._deserialize(params.get("Detail"))
        self.RequestId = params.get("RequestId")


class DescribeSlowQueryListRequest(AbstractModel):
    """DescribeSlowQueryList请求参数结构体

    """

    def __init__(self):
        r"""
        :param DBInstanceId: 实例ID。
        :type DBInstanceId: str
        :param StartTime: 查询起始时间戳，格式 “YYYY-MM-DD HH:mm:ss” ，日志保留时间默认为7天，起始时间不能超出保留时间范围。
        :type StartTime: str
        :param EndTime: 查询结束时间戳，格式 “YYYY-MM-DD HH:mm:ss”。
        :type EndTime: str
        :param DatabaseName: 根据数据库名进行筛选，可以为空。
        :type DatabaseName: str
        :param OrderByType: 排序类型。升序asc、降序desc。默认为desc。
        :type OrderByType: str
        :param OrderBy: 排序维度。 可选参数，取值范围[SessionStartTime,Duration]，默认为SessionStartTime。
        :type OrderBy: str
        :param Limit: 分页大小。取值范围[1,100],默认为20。
        :type Limit: int
        :param Offset: 分页偏移。取值范围[0,INF)，默认为0。
        :type Offset: int
        """
        self.DBInstanceId = None
        self.StartTime = None
        self.EndTime = None
        self.DatabaseName = None
        self.OrderByType = None
        self.OrderBy = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.DBInstanceId = params.get("DBInstanceId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.DatabaseName = params.get("DatabaseName")
        self.OrderByType = params.get("OrderByType")
        self.OrderBy = params.get("OrderBy")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSlowQueryListResponse(AbstractModel):
    """DescribeSlowQueryList返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 选定时间范围内慢SQL总条数。
        :type TotalCount: int
        :param DurationAnalysis: 指定时间范围内，慢SQL耗时分段分析。
注意：此字段可能返回 null，表示取不到有效值。
        :type DurationAnalysis: list of DurationAnalysis
        :param RawSlowQueryList: 指定时间范围内 慢SQL流水。
注意：此字段可能返回 null，表示取不到有效值。
        :type RawSlowQueryList: list of RawSlowQuery
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.DurationAnalysis = None
        self.RawSlowQueryList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("DurationAnalysis") is not None:
            self.DurationAnalysis = []
            for item in params.get("DurationAnalysis"):
                obj = DurationAnalysis()
                obj._deserialize(item)
                self.DurationAnalysis.append(obj)
        if params.get("RawSlowQueryList") is not None:
            self.RawSlowQueryList = []
            for item in params.get("RawSlowQueryList"):
                obj = RawSlowQuery()
                obj._deserialize(item)
                self.RawSlowQueryList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeZonesRequest(AbstractModel):
    """DescribeZones请求参数结构体

    """


class DescribeZonesResponse(AbstractModel):
    """DescribeZones返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 返回的结果数量。
        :type TotalCount: int
        :param ZoneSet: 可用区信息集合。
        :type ZoneSet: list of ZoneInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.ZoneSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("ZoneSet") is not None:
            self.ZoneSet = []
            for item in params.get("ZoneSet"):
                obj = ZoneInfo()
                obj._deserialize(item)
                self.ZoneSet.append(obj)
        self.RequestId = params.get("RequestId")


class DestroyDBInstanceRequest(AbstractModel):
    """DestroyDBInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param DBInstanceId: 待下线实例ID
        :type DBInstanceId: str
        """
        self.DBInstanceId = None


    def _deserialize(self, params):
        self.DBInstanceId = params.get("DBInstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DestroyDBInstanceResponse(AbstractModel):
    """DestroyDBInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class Detail(AbstractModel):
    """慢SQL 统计分析接口返回详情

    """

    def __init__(self):
        r"""
        :param TotalTime: 输入时间范围内所有慢sql执行的总时间，单位毫秒（ms）
        :type TotalTime: float
        :param TotalCallNum: 输入时间范围内所有慢sql总条数
        :type TotalCallNum: int
        :param AnalysisItems: 慢SQL统计分析列表
注意：此字段可能返回 null，表示取不到有效值。
        :type AnalysisItems: list of AnalysisItems
        """
        self.TotalTime = None
        self.TotalCallNum = None
        self.AnalysisItems = None


    def _deserialize(self, params):
        self.TotalTime = params.get("TotalTime")
        self.TotalCallNum = params.get("TotalCallNum")
        if params.get("AnalysisItems") is not None:
            self.AnalysisItems = []
            for item in params.get("AnalysisItems"):
                obj = AnalysisItems()
                obj._deserialize(item)
                self.AnalysisItems.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisIsolateDBInstancesRequest(AbstractModel):
    """DisIsolateDBInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param DBInstanceIdSet: 资源ID列表。注意：当前已不支持同时解隔离多个实例，这里只能传入单个实例ID。
        :type DBInstanceIdSet: list of str
        :param Period: 包年包月实例解隔离时购买时常 以月为单位
        :type Period: int
        :param AutoVoucher: 是否使用代金券：true-使用,false-不使用，默认不使用
        :type AutoVoucher: bool
        :param VoucherIds: 代金券id列表
        :type VoucherIds: list of str
        """
        self.DBInstanceIdSet = None
        self.Period = None
        self.AutoVoucher = None
        self.VoucherIds = None


    def _deserialize(self, params):
        self.DBInstanceIdSet = params.get("DBInstanceIdSet")
        self.Period = params.get("Period")
        self.AutoVoucher = params.get("AutoVoucher")
        self.VoucherIds = params.get("VoucherIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisIsolateDBInstancesResponse(AbstractModel):
    """DisIsolateDBInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DurationAnalysis(AbstractModel):
    """慢SQL耗时分段分析

    """

    def __init__(self):
        r"""
        :param TimeSegment: 慢SQL耗时，时段
        :type TimeSegment: str
        :param Count: 对应时段区间慢SQL 条数
        :type Count: int
        """
        self.TimeSegment = None
        self.Count = None


    def _deserialize(self, params):
        self.TimeSegment = params.get("TimeSegment")
        self.Count = params.get("Count")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EncryptionKey(AbstractModel):
    """KMS密钥信息

    """

    def __init__(self):
        r"""
        :param KeyId: KMS实例加密的KeyId。
注意：此字段可能返回 null，表示取不到有效值。
        :type KeyId: str
        :param KeyAlias: KMS实例加密Key的别名。
注意：此字段可能返回 null，表示取不到有效值。
        :type KeyAlias: str
        :param DEKCipherTextBlob: 实例加密密钥DEK的密文。
注意：此字段可能返回 null，表示取不到有效值。
        :type DEKCipherTextBlob: str
        :param IsEnabled: 密钥是否启用，1-启用， 0-未启用。
注意：此字段可能返回 null，表示取不到有效值。
        :type IsEnabled: int
        :param KeyRegion: KMS密钥所在地域。
注意：此字段可能返回 null，表示取不到有效值。
        :type KeyRegion: str
        :param CreateTime: DEK密钥创建时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        """
        self.KeyId = None
        self.KeyAlias = None
        self.DEKCipherTextBlob = None
        self.IsEnabled = None
        self.KeyRegion = None
        self.CreateTime = None


    def _deserialize(self, params):
        self.KeyId = params.get("KeyId")
        self.KeyAlias = params.get("KeyAlias")
        self.DEKCipherTextBlob = params.get("DEKCipherTextBlob")
        self.IsEnabled = params.get("IsEnabled")
        self.KeyRegion = params.get("KeyRegion")
        self.CreateTime = params.get("CreateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ErrLogDetail(AbstractModel):
    """错误日志详情

    """

    def __init__(self):
        r"""
        :param UserName: 用户名
        :type UserName: str
        :param Database: 数据库名字
        :type Database: str
        :param ErrTime: 错误发生时间
        :type ErrTime: str
        :param ErrMsg: 错误消息
        :type ErrMsg: str
        """
        self.UserName = None
        self.Database = None
        self.ErrTime = None
        self.ErrMsg = None


    def _deserialize(self, params):
        self.UserName = params.get("UserName")
        self.Database = params.get("Database")
        self.ErrTime = params.get("ErrTime")
        self.ErrMsg = params.get("ErrMsg")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EventInfo(AbstractModel):
    """参数修改事件信息

    """

    def __init__(self):
        r"""
        :param ParamName: 参数名
注意：此字段可能返回 null，表示取不到有效值。
        :type ParamName: str
        :param OldValue: 原参数值
注意：此字段可能返回 null，表示取不到有效值。
        :type OldValue: str
        :param NewValue: 本次修改期望参数值
注意：此字段可能返回 null，表示取不到有效值。
        :type NewValue: str
        :param ModifyTime: 后台参数修改开始时间
注意：此字段可能返回 null，表示取不到有效值。
        :type ModifyTime: str
        :param EffectiveTime: 后台参数生效开始时间
注意：此字段可能返回 null，表示取不到有效值。
        :type EffectiveTime: str
        :param State: 修改状态
注意：此字段可能返回 null，表示取不到有效值。
        :type State: str
        :param Operator: 操作者（一般为用户sub UIN）
注意：此字段可能返回 null，表示取不到有效值。
        :type Operator: str
        :param EventLog: 时间日志。
注意：此字段可能返回 null，表示取不到有效值。
        :type EventLog: str
        """
        self.ParamName = None
        self.OldValue = None
        self.NewValue = None
        self.ModifyTime = None
        self.EffectiveTime = None
        self.State = None
        self.Operator = None
        self.EventLog = None


    def _deserialize(self, params):
        self.ParamName = params.get("ParamName")
        self.OldValue = params.get("OldValue")
        self.NewValue = params.get("NewValue")
        self.ModifyTime = params.get("ModifyTime")
        self.EffectiveTime = params.get("EffectiveTime")
        self.State = params.get("State")
        self.Operator = params.get("Operator")
        self.EventLog = params.get("EventLog")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EventItem(AbstractModel):
    """修改参数条目，以参数为维度

    """

    def __init__(self):
        r"""
        :param ParamName: 参数名
注意：此字段可能返回 null，表示取不到有效值。
        :type ParamName: str
        :param EventCount: 修改事件数
注意：此字段可能返回 null，表示取不到有效值。
        :type EventCount: int
        :param EventDetail: 修改时间详情
注意：此字段可能返回 null，表示取不到有效值。
        :type EventDetail: list of EventInfo
        """
        self.ParamName = None
        self.EventCount = None
        self.EventDetail = None


    def _deserialize(self, params):
        self.ParamName = params.get("ParamName")
        self.EventCount = params.get("EventCount")
        if params.get("EventDetail") is not None:
            self.EventDetail = []
            for item in params.get("EventDetail"):
                obj = EventInfo()
                obj._deserialize(item)
                self.EventDetail.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Filter(AbstractModel):
    """描述键值对过滤器，用于条件过滤查询。例如过滤ID、名称等
    * 若存在多个Filter时，Filter间的关系为逻辑与（AND）关系。
    * 若同一个Filter存在多个Values，同一Filter下Values间的关系为逻辑或（OR）关系。

    """

    def __init__(self):
        r"""
        :param Name: 过滤键的名称。
        :type Name: str
        :param Values: 一个或者多个过滤值。
        :type Values: list of str
        """
        self.Name = None
        self.Values = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Values = params.get("Values")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InitDBInstancesRequest(AbstractModel):
    """InitDBInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param DBInstanceIdSet: 实例ID集合。
        :type DBInstanceIdSet: list of str
        :param AdminName: 实例根账号用户名。
        :type AdminName: str
        :param AdminPassword: 实例根账号用户名对应的密码。
        :type AdminPassword: str
        :param Charset: 实例字符集，目前只支持：UTF8、LATIN1。
        :type Charset: str
        """
        self.DBInstanceIdSet = None
        self.AdminName = None
        self.AdminPassword = None
        self.Charset = None


    def _deserialize(self, params):
        self.DBInstanceIdSet = params.get("DBInstanceIdSet")
        self.AdminName = params.get("AdminName")
        self.AdminPassword = params.get("AdminPassword")
        self.Charset = params.get("Charset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InitDBInstancesResponse(AbstractModel):
    """InitDBInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param DBInstanceIdSet: 实例ID集合。
        :type DBInstanceIdSet: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DBInstanceIdSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DBInstanceIdSet = params.get("DBInstanceIdSet")
        self.RequestId = params.get("RequestId")


class InquiryPriceCreateDBInstancesRequest(AbstractModel):
    """InquiryPriceCreateDBInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param Zone: 可用区ID。该参数可以通过调用 DescribeZones 接口的返回值中的Zone字段来获取。
        :type Zone: str
        :param SpecCode: 规格ID。该参数可以通过调用DescribeProductConfig接口的返回值中的SpecCode字段来获取。
        :type SpecCode: str
        :param Storage: 存储容量大小，单位：GB。
        :type Storage: int
        :param InstanceCount: 实例数量。目前最大数量不超过100，如需一次性创建更多实例，请联系客服支持。
        :type InstanceCount: int
        :param Period: 购买时长，单位：月。目前只支持1,2,3,4,5,6,7,8,9,10,11,12,24,36这些值。
        :type Period: int
        :param Pid: 【弃字段，不再生效】，计费ID。该参数可以通过调用DescribeProductConfig接口的返回值中的Pid字段来获取。
        :type Pid: int
        :param InstanceChargeType: 实例计费类型。目前只支持：PREPAID（预付费，即包年包月）。
        :type InstanceChargeType: str
        :param InstanceType: 实例类型，默认primary，支持如下：
primary（双机高可用（一主一从））
readonly（只读实例）
        :type InstanceType: str
        :param DBEngine: DB引擎，默认postgresql，支持如下：
postgresql（云数据库PostgreSQL）
mssql_compatible（MSSQL兼容-云数据库PostgreSQL）
        :type DBEngine: str
        """
        self.Zone = None
        self.SpecCode = None
        self.Storage = None
        self.InstanceCount = None
        self.Period = None
        self.Pid = None
        self.InstanceChargeType = None
        self.InstanceType = None
        self.DBEngine = None


    def _deserialize(self, params):
        self.Zone = params.get("Zone")
        self.SpecCode = params.get("SpecCode")
        self.Storage = params.get("Storage")
        self.InstanceCount = params.get("InstanceCount")
        self.Period = params.get("Period")
        self.Pid = params.get("Pid")
        self.InstanceChargeType = params.get("InstanceChargeType")
        self.InstanceType = params.get("InstanceType")
        self.DBEngine = params.get("DBEngine")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquiryPriceCreateDBInstancesResponse(AbstractModel):
    """InquiryPriceCreateDBInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param OriginalPrice: 刊例价，单位：分
        :type OriginalPrice: int
        :param Price: 折后实际付款金额，单位：分
        :type Price: int
        :param Currency: 币种。例如，CNY：人民币。
        :type Currency: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.OriginalPrice = None
        self.Price = None
        self.Currency = None
        self.RequestId = None


    def _deserialize(self, params):
        self.OriginalPrice = params.get("OriginalPrice")
        self.Price = params.get("Price")
        self.Currency = params.get("Currency")
        self.RequestId = params.get("RequestId")


class InquiryPriceRenewDBInstanceRequest(AbstractModel):
    """InquiryPriceRenewDBInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param DBInstanceId: 实例ID
        :type DBInstanceId: str
        :param Period: 续费周期，按月计算，最大不超过48
        :type Period: int
        """
        self.DBInstanceId = None
        self.Period = None


    def _deserialize(self, params):
        self.DBInstanceId = params.get("DBInstanceId")
        self.Period = params.get("Period")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquiryPriceRenewDBInstanceResponse(AbstractModel):
    """InquiryPriceRenewDBInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param OriginalPrice: 刊例价，单位为分。如24650表示246.5元
        :type OriginalPrice: int
        :param Price: 折后实际付款金额，单位为分。如24650表示246.5元
        :type Price: int
        :param Currency: 币种。例如，CNY：人民币。
        :type Currency: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.OriginalPrice = None
        self.Price = None
        self.Currency = None
        self.RequestId = None


    def _deserialize(self, params):
        self.OriginalPrice = params.get("OriginalPrice")
        self.Price = params.get("Price")
        self.Currency = params.get("Currency")
        self.RequestId = params.get("RequestId")


class InquiryPriceUpgradeDBInstanceRequest(AbstractModel):
    """InquiryPriceUpgradeDBInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param Storage: 实例的磁盘大小，单位GB
        :type Storage: int
        :param Memory: 实例的内存大小，单位GB
        :type Memory: int
        :param DBInstanceId: 实例ID，形如postgres-hez4fh0v
        :type DBInstanceId: str
        :param InstanceChargeType: 【废弃参数，不再生效】，实例计费类型。
        :type InstanceChargeType: str
        """
        self.Storage = None
        self.Memory = None
        self.DBInstanceId = None
        self.InstanceChargeType = None


    def _deserialize(self, params):
        self.Storage = params.get("Storage")
        self.Memory = params.get("Memory")
        self.DBInstanceId = params.get("DBInstanceId")
        self.InstanceChargeType = params.get("InstanceChargeType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquiryPriceUpgradeDBInstanceResponse(AbstractModel):
    """InquiryPriceUpgradeDBInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param OriginalPrice: 刊例价费用
        :type OriginalPrice: int
        :param Price: 折后实际付款金额
        :type Price: int
        :param Currency: 币种。例如，CNY：人民币。
        :type Currency: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.OriginalPrice = None
        self.Price = None
        self.Currency = None
        self.RequestId = None


    def _deserialize(self, params):
        self.OriginalPrice = params.get("OriginalPrice")
        self.Price = params.get("Price")
        self.Currency = params.get("Currency")
        self.RequestId = params.get("RequestId")


class IsolateDBInstancesRequest(AbstractModel):
    """IsolateDBInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param DBInstanceIdSet: 实例ID集合。注意：当前已不支持同时隔离多个实例，这里只能传入单个实例ID。
        :type DBInstanceIdSet: list of str
        """
        self.DBInstanceIdSet = None


    def _deserialize(self, params):
        self.DBInstanceIdSet = params.get("DBInstanceIdSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IsolateDBInstancesResponse(AbstractModel):
    """IsolateDBInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class LogBackup(AbstractModel):
    """数据库日志备份信息

    """

    def __init__(self):
        r"""
        :param DBInstanceId: 实例ID。
        :type DBInstanceId: str
        :param Id: 备份文件唯一标识。
        :type Id: str
        :param Name: 备份文件名称。
        :type Name: str
        :param BackupMethod: 备份方式：物理备份、逻辑备份。
        :type BackupMethod: str
        :param BackupMode: 备份模式：自动备份、手动备份。
        :type BackupMode: str
        :param State: 备份任务状态。
        :type State: str
        :param Size: 备份集大小，单位bytes。
        :type Size: int
        :param StartTime: 备份的开始时间。
        :type StartTime: str
        :param FinishTime: 备份的结束时间。
        :type FinishTime: str
        :param ExpireTime: 备份的过期时间。
        :type ExpireTime: str
        """
        self.DBInstanceId = None
        self.Id = None
        self.Name = None
        self.BackupMethod = None
        self.BackupMode = None
        self.State = None
        self.Size = None
        self.StartTime = None
        self.FinishTime = None
        self.ExpireTime = None


    def _deserialize(self, params):
        self.DBInstanceId = params.get("DBInstanceId")
        self.Id = params.get("Id")
        self.Name = params.get("Name")
        self.BackupMethod = params.get("BackupMethod")
        self.BackupMode = params.get("BackupMode")
        self.State = params.get("State")
        self.Size = params.get("Size")
        self.StartTime = params.get("StartTime")
        self.FinishTime = params.get("FinishTime")
        self.ExpireTime = params.get("ExpireTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAccountRemarkRequest(AbstractModel):
    """ModifyAccountRemark请求参数结构体

    """

    def __init__(self):
        r"""
        :param DBInstanceId: 实例ID，形如postgres-4wdeb0zv
        :type DBInstanceId: str
        :param UserName: 实例用户名
        :type UserName: str
        :param Remark: 用户UserName对应的新备注
        :type Remark: str
        """
        self.DBInstanceId = None
        self.UserName = None
        self.Remark = None


    def _deserialize(self, params):
        self.DBInstanceId = params.get("DBInstanceId")
        self.UserName = params.get("UserName")
        self.Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAccountRemarkResponse(AbstractModel):
    """ModifyAccountRemark返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyBackupDownloadRestrictionRequest(AbstractModel):
    """ModifyBackupDownloadRestriction请求参数结构体

    """

    def __init__(self):
        r"""
        :param RestrictionType: 备份文件下载限制类型，NONE 无限制，内外网都可以下载；INTRANET 只允许内网下载；CUSTOMIZE 自定义限制下载的vpc或ip。
        :type RestrictionType: str
        :param VpcRestrictionEffect: vpc限制效力，ALLOW 允许；DENY 拒绝。
        :type VpcRestrictionEffect: str
        :param VpcIdSet: 允许或拒绝下载备份文件的vpcId列表。
        :type VpcIdSet: list of str
        :param IpRestrictionEffect: ip限制效力，ALLOW 允许；DENY 拒绝。
        :type IpRestrictionEffect: str
        :param IpSet: 允许或拒绝下载备份文件的ip列表。
        :type IpSet: list of str
        """
        self.RestrictionType = None
        self.VpcRestrictionEffect = None
        self.VpcIdSet = None
        self.IpRestrictionEffect = None
        self.IpSet = None


    def _deserialize(self, params):
        self.RestrictionType = params.get("RestrictionType")
        self.VpcRestrictionEffect = params.get("VpcRestrictionEffect")
        self.VpcIdSet = params.get("VpcIdSet")
        self.IpRestrictionEffect = params.get("IpRestrictionEffect")
        self.IpSet = params.get("IpSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyBackupDownloadRestrictionResponse(AbstractModel):
    """ModifyBackupDownloadRestriction返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyBackupPlanRequest(AbstractModel):
    """ModifyBackupPlan请求参数结构体

    """

    def __init__(self):
        r"""
        :param DBInstanceId: 实例ID
        :type DBInstanceId: str
        :param MinBackupStartTime: 实例最早开始备份时间
        :type MinBackupStartTime: str
        :param MaxBackupStartTime: 实例最晚开始备份时间
        :type MaxBackupStartTime: str
        :param BaseBackupRetentionPeriod: 实例备份保留时长，取值范围为3-7，单位是天
        :type BaseBackupRetentionPeriod: int
        :param BackupPeriod: 实例备份周期，按照星期维度，格式为小写星期英文单词
        :type BackupPeriod: list of str
        """
        self.DBInstanceId = None
        self.MinBackupStartTime = None
        self.MaxBackupStartTime = None
        self.BaseBackupRetentionPeriod = None
        self.BackupPeriod = None


    def _deserialize(self, params):
        self.DBInstanceId = params.get("DBInstanceId")
        self.MinBackupStartTime = params.get("MinBackupStartTime")
        self.MaxBackupStartTime = params.get("MaxBackupStartTime")
        self.BaseBackupRetentionPeriod = params.get("BaseBackupRetentionPeriod")
        self.BackupPeriod = params.get("BackupPeriod")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyBackupPlanResponse(AbstractModel):
    """ModifyBackupPlan返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyBaseBackupExpireTimeRequest(AbstractModel):
    """ModifyBaseBackupExpireTime请求参数结构体

    """

    def __init__(self):
        r"""
        :param DBInstanceId: 实例ID。
        :type DBInstanceId: str
        :param BaseBackupId: 基础备份ID。
        :type BaseBackupId: str
        :param NewExpireTime: 新过期时间。
        :type NewExpireTime: str
        """
        self.DBInstanceId = None
        self.BaseBackupId = None
        self.NewExpireTime = None


    def _deserialize(self, params):
        self.DBInstanceId = params.get("DBInstanceId")
        self.BaseBackupId = params.get("BaseBackupId")
        self.NewExpireTime = params.get("NewExpireTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyBaseBackupExpireTimeResponse(AbstractModel):
    """ModifyBaseBackupExpireTime返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyDBInstanceChargeTypeRequest(AbstractModel):
    """ModifyDBInstanceChargeType请求参数结构体

    """

    def __init__(self):
        r"""
        :param DBInstanceId: 实例ID，形如postgres-6fego161
        :type DBInstanceId: str
        :param InstanceChargeType: 实例计费类型。目前支持：PREPAID（预付费，即包年包月），POSTPAID_BY_HOUR（后付费，即按量计费）。默认值：PREPAID。
        :type InstanceChargeType: str
        :param Period: 购买时长，单位：月。目前只支持1,2,3,4,5,6,7,8,9,10,11,12,24,36这些值，按量计费模式下该参数传1。
        :type Period: int
        :param AutoRenewFlag: 续费标记：0-正常续费（默认）；1-自动续费。
        :type AutoRenewFlag: int
        :param AutoVoucher: 是否自动使用代金券,1是,0否，默认不使用
        :type AutoVoucher: int
        """
        self.DBInstanceId = None
        self.InstanceChargeType = None
        self.Period = None
        self.AutoRenewFlag = None
        self.AutoVoucher = None


    def _deserialize(self, params):
        self.DBInstanceId = params.get("DBInstanceId")
        self.InstanceChargeType = params.get("InstanceChargeType")
        self.Period = params.get("Period")
        self.AutoRenewFlag = params.get("AutoRenewFlag")
        self.AutoVoucher = params.get("AutoVoucher")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDBInstanceChargeTypeResponse(AbstractModel):
    """ModifyDBInstanceChargeType返回参数结构体

    """

    def __init__(self):
        r"""
        :param DealName: 订单名
        :type DealName: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DealName = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DealName = params.get("DealName")
        self.RequestId = params.get("RequestId")


class ModifyDBInstanceDeploymentRequest(AbstractModel):
    """ModifyDBInstanceDeployment请求参数结构体

    """

    def __init__(self):
        r"""
        :param DBInstanceId: 实例ID。
        :type DBInstanceId: str
        :param DBNodeSet: 实例节点信息。
        :type DBNodeSet: list of DBNode
        :param SwitchTag: 切换时间。默认为 立即切换，入参为 0 ：立即切换 。1：指定时间切换。2：维护时间窗口内切换
        :type SwitchTag: int
        :param SwitchStartTime: 切换开始时间，时间格式：HH:MM:SS，例如：01:00:00。当SwitchTag为0或2时，该参数失效。
        :type SwitchStartTime: str
        :param SwitchEndTime: 切换截止时间，时间格式：HH:MM:SS，例如：01:30:00。当SwitchTag为0或2时，该参数失效。
        :type SwitchEndTime: str
        """
        self.DBInstanceId = None
        self.DBNodeSet = None
        self.SwitchTag = None
        self.SwitchStartTime = None
        self.SwitchEndTime = None


    def _deserialize(self, params):
        self.DBInstanceId = params.get("DBInstanceId")
        if params.get("DBNodeSet") is not None:
            self.DBNodeSet = []
            for item in params.get("DBNodeSet"):
                obj = DBNode()
                obj._deserialize(item)
                self.DBNodeSet.append(obj)
        self.SwitchTag = params.get("SwitchTag")
        self.SwitchStartTime = params.get("SwitchStartTime")
        self.SwitchEndTime = params.get("SwitchEndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDBInstanceDeploymentResponse(AbstractModel):
    """ModifyDBInstanceDeployment返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyDBInstanceNameRequest(AbstractModel):
    """ModifyDBInstanceName请求参数结构体

    """

    def __init__(self):
        r"""
        :param DBInstanceId: 数据库实例ID，形如postgres-6fego161
        :type DBInstanceId: str
        :param InstanceName: 新的数据库实例名字
        :type InstanceName: str
        """
        self.DBInstanceId = None
        self.InstanceName = None


    def _deserialize(self, params):
        self.DBInstanceId = params.get("DBInstanceId")
        self.InstanceName = params.get("InstanceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDBInstanceNameResponse(AbstractModel):
    """ModifyDBInstanceName返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyDBInstanceParametersRequest(AbstractModel):
    """ModifyDBInstanceParameters请求参数结构体

    """

    def __init__(self):
        r"""
        :param DBInstanceId: 实例ID
        :type DBInstanceId: str
        :param ParamList: 待修改参数及期望值
        :type ParamList: list of ParamEntry
        """
        self.DBInstanceId = None
        self.ParamList = None


    def _deserialize(self, params):
        self.DBInstanceId = params.get("DBInstanceId")
        if params.get("ParamList") is not None:
            self.ParamList = []
            for item in params.get("ParamList"):
                obj = ParamEntry()
                obj._deserialize(item)
                self.ParamList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDBInstanceParametersResponse(AbstractModel):
    """ModifyDBInstanceParameters返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyDBInstanceReadOnlyGroupRequest(AbstractModel):
    """ModifyDBInstanceReadOnlyGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param DBInstanceId: 实例ID
        :type DBInstanceId: str
        :param ReadOnlyGroupId: 当前实例所在只读组ID
        :type ReadOnlyGroupId: str
        :param NewReadOnlyGroupId: 实例修改的目标只读组ID
        :type NewReadOnlyGroupId: str
        """
        self.DBInstanceId = None
        self.ReadOnlyGroupId = None
        self.NewReadOnlyGroupId = None


    def _deserialize(self, params):
        self.DBInstanceId = params.get("DBInstanceId")
        self.ReadOnlyGroupId = params.get("ReadOnlyGroupId")
        self.NewReadOnlyGroupId = params.get("NewReadOnlyGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDBInstanceReadOnlyGroupResponse(AbstractModel):
    """ModifyDBInstanceReadOnlyGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param FlowId: 流程ID
        :type FlowId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.FlowId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        self.RequestId = params.get("RequestId")


class ModifyDBInstanceSecurityGroupsRequest(AbstractModel):
    """ModifyDBInstanceSecurityGroups请求参数结构体

    """

    def __init__(self):
        r"""
        :param SecurityGroupIdSet: 实例或只读组要绑定的安全组列表
        :type SecurityGroupIdSet: list of str
        :param DBInstanceId: 实例ID，DBInstanceId和ReadOnlyGroupId至少传一个；如果都传，忽略ReadOnlyGroupId
        :type DBInstanceId: str
        :param ReadOnlyGroupId: 只读组ID，DBInstanceId和ReadOnlyGroupId至少传一个；如果要修改只读组关联的安全组，只传ReadOnlyGroupId
        :type ReadOnlyGroupId: str
        """
        self.SecurityGroupIdSet = None
        self.DBInstanceId = None
        self.ReadOnlyGroupId = None


    def _deserialize(self, params):
        self.SecurityGroupIdSet = params.get("SecurityGroupIdSet")
        self.DBInstanceId = params.get("DBInstanceId")
        self.ReadOnlyGroupId = params.get("ReadOnlyGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDBInstanceSecurityGroupsResponse(AbstractModel):
    """ModifyDBInstanceSecurityGroups返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyDBInstanceSpecRequest(AbstractModel):
    """ModifyDBInstanceSpec请求参数结构体

    """

    def __init__(self):
        r"""
        :param DBInstanceId: 实例ID，形如：postgres-6bwgamo3。
        :type DBInstanceId: str
        :param Memory: 修改后的实例内存大小，单位GiB。
        :type Memory: int
        :param Storage: 修改后的实例磁盘大小，单位GiB。
        :type Storage: int
        :param AutoVoucher: 是否自动使用代金券,1是,0否，默认不使用。
        :type AutoVoucher: int
        :param VoucherIds: 代金券ID列表，目前仅支持指定一张代金券。
        :type VoucherIds: list of str
        :param ActivityId: 活动ID。
        :type ActivityId: int
        :param SwitchTag: 指定实例配置完成变更后的切换时间，默认为 立即切换，入参为 0 ：立即切换 。1：指定时间切换。2：维护时间窗口内切换。
        :type SwitchTag: int
        :param SwitchStartTime: 切换开始时间，时间格式：HH:MM:SS，例如：01:00:00。当SwitchTag为0或2时，该参数失效。
        :type SwitchStartTime: str
        :param SwitchEndTime: 切换截止时间，时间格式：HH:MM:SS，例如：01:30:00。当SwitchTag为0或2时，该参数失效。
        :type SwitchEndTime: str
        """
        self.DBInstanceId = None
        self.Memory = None
        self.Storage = None
        self.AutoVoucher = None
        self.VoucherIds = None
        self.ActivityId = None
        self.SwitchTag = None
        self.SwitchStartTime = None
        self.SwitchEndTime = None


    def _deserialize(self, params):
        self.DBInstanceId = params.get("DBInstanceId")
        self.Memory = params.get("Memory")
        self.Storage = params.get("Storage")
        self.AutoVoucher = params.get("AutoVoucher")
        self.VoucherIds = params.get("VoucherIds")
        self.ActivityId = params.get("ActivityId")
        self.SwitchTag = params.get("SwitchTag")
        self.SwitchStartTime = params.get("SwitchStartTime")
        self.SwitchEndTime = params.get("SwitchEndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDBInstanceSpecResponse(AbstractModel):
    """ModifyDBInstanceSpec返回参数结构体

    """

    def __init__(self):
        r"""
        :param DealName: 订单号。
        :type DealName: str
        :param BillId: 冻结流水号。
        :type BillId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DealName = None
        self.BillId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DealName = params.get("DealName")
        self.BillId = params.get("BillId")
        self.RequestId = params.get("RequestId")


class ModifyDBInstancesProjectRequest(AbstractModel):
    """ModifyDBInstancesProject请求参数结构体

    """

    def __init__(self):
        r"""
        :param DBInstanceIdSet: 实例ID集合。注意：当前已不支持同时操作多个实例，这里只能传入单个实例ID。
        :type DBInstanceIdSet: list of str
        :param ProjectId: 所属新项目的ID
        :type ProjectId: str
        """
        self.DBInstanceIdSet = None
        self.ProjectId = None


    def _deserialize(self, params):
        self.DBInstanceIdSet = params.get("DBInstanceIdSet")
        self.ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDBInstancesProjectResponse(AbstractModel):
    """ModifyDBInstancesProject返回参数结构体

    """

    def __init__(self):
        r"""
        :param Count: 转移项目成功的实例个数
        :type Count: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Count = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Count = params.get("Count")
        self.RequestId = params.get("RequestId")


class ModifyParameterTemplateRequest(AbstractModel):
    """ModifyParameterTemplate请求参数结构体

    """

    def __init__(self):
        r"""
        :param TemplateId: 参数模板ID，用于唯一确认参数模板，不可修改
        :type TemplateId: str
        :param TemplateName: 参数模板名称，长度为1～60个字符，仅支持数字,英文大小写字母、中文以及特殊字符_-./()（）[]+=：:@  注：若该字段为空    ，则保持原参数模板名称
        :type TemplateName: str
        :param TemplateDescription: 参数模板描述，长度为0～60个字符，仅支持数字,英文大小写字母、中文以及特殊字符_-./()（）[]+=：:@  注：若不传入该参数，则保持原参数模板描述
        :type TemplateDescription: str
        :param ModifyParamEntrySet: 需要修改或添加的参数集合，注：同一参数不能同时出现在修改添加集合和删除集合中
        :type ModifyParamEntrySet: list of ParamEntry
        :param DeleteParamSet: 需要从模板中删除的参数集合，注：同一参数不能同时出现在修改添加集合和删除集合中
        :type DeleteParamSet: list of str
        """
        self.TemplateId = None
        self.TemplateName = None
        self.TemplateDescription = None
        self.ModifyParamEntrySet = None
        self.DeleteParamSet = None


    def _deserialize(self, params):
        self.TemplateId = params.get("TemplateId")
        self.TemplateName = params.get("TemplateName")
        self.TemplateDescription = params.get("TemplateDescription")
        if params.get("ModifyParamEntrySet") is not None:
            self.ModifyParamEntrySet = []
            for item in params.get("ModifyParamEntrySet"):
                obj = ParamEntry()
                obj._deserialize(item)
                self.ModifyParamEntrySet.append(obj)
        self.DeleteParamSet = params.get("DeleteParamSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyParameterTemplateResponse(AbstractModel):
    """ModifyParameterTemplate返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyReadOnlyGroupConfigRequest(AbstractModel):
    """ModifyReadOnlyGroupConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param ReadOnlyGroupId: 只读组ID
        :type ReadOnlyGroupId: str
        :param ReadOnlyGroupName: 只读组名称
        :type ReadOnlyGroupName: str
        :param ReplayLagEliminate: 延迟时间配置开关：0关、1开
        :type ReplayLagEliminate: int
        :param ReplayLatencyEliminate: 延迟日志大小配置开关：0关、1开
        :type ReplayLatencyEliminate: int
        :param MaxReplayLatency: 延迟日志大小阈值，单位MB
        :type MaxReplayLatency: int
        :param MaxReplayLag: 延迟时间大小阈值，单位ms
        :type MaxReplayLag: int
        :param Rebalance: 自动负载均衡开关：0关、1开
        :type Rebalance: int
        :param MinDelayEliminateReserve: 延迟剔除最小保留实例数
        :type MinDelayEliminateReserve: int
        """
        self.ReadOnlyGroupId = None
        self.ReadOnlyGroupName = None
        self.ReplayLagEliminate = None
        self.ReplayLatencyEliminate = None
        self.MaxReplayLatency = None
        self.MaxReplayLag = None
        self.Rebalance = None
        self.MinDelayEliminateReserve = None


    def _deserialize(self, params):
        self.ReadOnlyGroupId = params.get("ReadOnlyGroupId")
        self.ReadOnlyGroupName = params.get("ReadOnlyGroupName")
        self.ReplayLagEliminate = params.get("ReplayLagEliminate")
        self.ReplayLatencyEliminate = params.get("ReplayLatencyEliminate")
        self.MaxReplayLatency = params.get("MaxReplayLatency")
        self.MaxReplayLag = params.get("MaxReplayLag")
        self.Rebalance = params.get("Rebalance")
        self.MinDelayEliminateReserve = params.get("MinDelayEliminateReserve")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyReadOnlyGroupConfigResponse(AbstractModel):
    """ModifyReadOnlyGroupConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifySwitchTimePeriodRequest(AbstractModel):
    """ModifySwitchTimePeriod请求参数结构体

    """

    def __init__(self):
        r"""
        :param DBInstanceId: 处于等待切换状态中的实例ID
        :type DBInstanceId: str
        :param SwitchTag: 入参取值为 0 ，代表立即切换。
        :type SwitchTag: int
        """
        self.DBInstanceId = None
        self.SwitchTag = None


    def _deserialize(self, params):
        self.DBInstanceId = params.get("DBInstanceId")
        self.SwitchTag = params.get("SwitchTag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifySwitchTimePeriodResponse(AbstractModel):
    """ModifySwitchTimePeriod返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class NetworkAccess(AbstractModel):
    """网络相关信息。（该数据结构已废弃，网络相关信息使用DBInstanceNetInfo）

    """

    def __init__(self):
        r"""
        :param ResourceId: 网络资源id，实例id或RO组id
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceId: str
        :param ResourceType: 资源类型，1-实例 2-RO组
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceType: int
        :param VpcId: 私有网络ID
注意：此字段可能返回 null，表示取不到有效值。
        :type VpcId: str
        :param Vip: IPV4地址
注意：此字段可能返回 null，表示取不到有效值。
        :type Vip: str
        :param Vip6: IPV6地址
注意：此字段可能返回 null，表示取不到有效值。
        :type Vip6: str
        :param Vport: 访问端口
注意：此字段可能返回 null，表示取不到有效值。
        :type Vport: int
        :param SubnetId: 子网ID
注意：此字段可能返回 null，表示取不到有效值。
        :type SubnetId: str
        :param VpcStatus: 网络状态，1-申请中，2-使用中，3-删除中，4-已删除
注意：此字段可能返回 null，表示取不到有效值。
        :type VpcStatus: int
        """
        self.ResourceId = None
        self.ResourceType = None
        self.VpcId = None
        self.Vip = None
        self.Vip6 = None
        self.Vport = None
        self.SubnetId = None
        self.VpcStatus = None


    def _deserialize(self, params):
        self.ResourceId = params.get("ResourceId")
        self.ResourceType = params.get("ResourceType")
        self.VpcId = params.get("VpcId")
        self.Vip = params.get("Vip")
        self.Vip6 = params.get("Vip6")
        self.Vport = params.get("Vport")
        self.SubnetId = params.get("SubnetId")
        self.VpcStatus = params.get("VpcStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NormalQueryItem(AbstractModel):
    """单条SlowQuery信息

    """

    def __init__(self):
        r"""
        :param UserName: 用户名
        :type UserName: str
        :param Calls: 调用次数
        :type Calls: int
        :param CallsGrids: 粒度点
        :type CallsGrids: list of int
        :param CostTime: 花费总时间
        :type CostTime: float
        :param Rows: 影响的行数
        :type Rows: int
        :param MinCostTime: 花费最小时间
        :type MinCostTime: float
        :param MaxCostTime: 花费最大时间
        :type MaxCostTime: float
        :param FirstTime: 最早一条慢SQL时间
        :type FirstTime: str
        :param LastTime: 最晚一条慢SQL时间
        :type LastTime: str
        :param SharedReadBlks: 读共享内存块数
        :type SharedReadBlks: int
        :param SharedWriteBlks: 写共享内存块数
        :type SharedWriteBlks: int
        :param ReadCostTime: 读io总耗时
        :type ReadCostTime: int
        :param WriteCostTime: 写io总耗时
        :type WriteCostTime: int
        :param DatabaseName: 数据库名字
        :type DatabaseName: str
        :param NormalQuery: 脱敏后的慢SQL
        :type NormalQuery: str
        """
        self.UserName = None
        self.Calls = None
        self.CallsGrids = None
        self.CostTime = None
        self.Rows = None
        self.MinCostTime = None
        self.MaxCostTime = None
        self.FirstTime = None
        self.LastTime = None
        self.SharedReadBlks = None
        self.SharedWriteBlks = None
        self.ReadCostTime = None
        self.WriteCostTime = None
        self.DatabaseName = None
        self.NormalQuery = None


    def _deserialize(self, params):
        self.UserName = params.get("UserName")
        self.Calls = params.get("Calls")
        self.CallsGrids = params.get("CallsGrids")
        self.CostTime = params.get("CostTime")
        self.Rows = params.get("Rows")
        self.MinCostTime = params.get("MinCostTime")
        self.MaxCostTime = params.get("MaxCostTime")
        self.FirstTime = params.get("FirstTime")
        self.LastTime = params.get("LastTime")
        self.SharedReadBlks = params.get("SharedReadBlks")
        self.SharedWriteBlks = params.get("SharedWriteBlks")
        self.ReadCostTime = params.get("ReadCostTime")
        self.WriteCostTime = params.get("WriteCostTime")
        self.DatabaseName = params.get("DatabaseName")
        self.NormalQuery = params.get("NormalQuery")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OpenDBExtranetAccessRequest(AbstractModel):
    """OpenDBExtranetAccess请求参数结构体

    """

    def __init__(self):
        r"""
        :param DBInstanceId: 实例ID，形如postgres-hez4fh0v
        :type DBInstanceId: str
        :param IsIpv6: 是否开通Ipv6外网，1：是，0：否
        :type IsIpv6: int
        """
        self.DBInstanceId = None
        self.IsIpv6 = None


    def _deserialize(self, params):
        self.DBInstanceId = params.get("DBInstanceId")
        self.IsIpv6 = params.get("IsIpv6")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OpenDBExtranetAccessResponse(AbstractModel):
    """OpenDBExtranetAccess返回参数结构体

    """

    def __init__(self):
        r"""
        :param FlowId: 异步任务流程ID
        :type FlowId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.FlowId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        self.RequestId = params.get("RequestId")


class OpenServerlessDBExtranetAccessRequest(AbstractModel):
    """OpenServerlessDBExtranetAccess请求参数结构体

    """

    def __init__(self):
        r"""
        :param DBInstanceId: 实例的唯一标识符
        :type DBInstanceId: str
        :param DBInstanceName: 实例名称
        :type DBInstanceName: str
        """
        self.DBInstanceId = None
        self.DBInstanceName = None


    def _deserialize(self, params):
        self.DBInstanceId = params.get("DBInstanceId")
        self.DBInstanceName = params.get("DBInstanceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OpenServerlessDBExtranetAccessResponse(AbstractModel):
    """OpenServerlessDBExtranetAccess返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ParamEntry(AbstractModel):
    """批量修改参数

    """

    def __init__(self):
        r"""
        :param Name: 参数名
        :type Name: str
        :param ExpectedValue: 修改参数值。入参均以字符串形式传递，例如：小数”0.1“、整数”1000“、枚举”replica“
        :type ExpectedValue: str
        """
        self.Name = None
        self.ExpectedValue = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.ExpectedValue = params.get("ExpectedValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ParamInfo(AbstractModel):
    """参数详情

    """

    def __init__(self):
        r"""
        :param ID: 参数ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ID: int
        :param Name: 参数名
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param ParamValueType: 参数值类型：integer（整型）、real（浮点型）、bool（布尔型）、enum（枚举类型）、mutil_enum（枚举类型、支持多选）。
当参数类型为integer（整型）、real（浮点型）时，参数的取值范围根据返回值的Max、Min确定； 
当参数类型为bool（布尔型）时，参数设置值取值范围是true | false； 
当参数类型为enum（枚举类型）、mutil_enum（多枚举类型）时，参数的取值范围由返回值中的EnumValue确定。
注意：此字段可能返回 null，表示取不到有效值。
        :type ParamValueType: str
        :param Unit: 参数值 单位。参数没有单位时，该字段返回空
注意：此字段可能返回 null，表示取不到有效值。
        :type Unit: str
        :param DefaultValue: 参数默认值。以字符串形式返回
注意：此字段可能返回 null，表示取不到有效值。
        :type DefaultValue: str
        :param CurrentValue: 参数当前运行值。以字符串形式返回
注意：此字段可能返回 null，表示取不到有效值。
        :type CurrentValue: str
        :param Max: 数值类型（integer、real）参数，取值下界
注意：此字段可能返回 null，表示取不到有效值。
        :type Max: float
        :param EnumValue: 枚举类型参数，取值范围
注意：此字段可能返回 null，表示取不到有效值。
        :type EnumValue: list of str
        :param Min: 数值类型（integer、real）参数，取值上界
注意：此字段可能返回 null，表示取不到有效值。
        :type Min: float
        :param ParamDescriptionCH: 参数中文描述
注意：此字段可能返回 null，表示取不到有效值。
        :type ParamDescriptionCH: str
        :param ParamDescriptionEN: 参数英文描述
注意：此字段可能返回 null，表示取不到有效值。
        :type ParamDescriptionEN: str
        :param NeedReboot: 参数修改，是否重启生效。（true为需要，false为不需要）
注意：此字段可能返回 null，表示取不到有效值。
        :type NeedReboot: bool
        :param ClassificationCN: 参数中文分类
注意：此字段可能返回 null，表示取不到有效值。
        :type ClassificationCN: str
        :param ClassificationEN: 参数英文分类
注意：此字段可能返回 null，表示取不到有效值。
        :type ClassificationEN: str
        :param SpecRelated: 是否和规格相关。（true为相关，false为不想关）
注意：此字段可能返回 null，表示取不到有效值。
        :type SpecRelated: bool
        :param Advanced: 是否为重点参数。（true为重点参数，修改是需要重点关注，可能会影响实例性能）
注意：此字段可能返回 null，表示取不到有效值。
        :type Advanced: bool
        :param LastModifyTime: 参数最后一次修改时间
注意：此字段可能返回 null，表示取不到有效值。
        :type LastModifyTime: str
        :param StandbyRelated: 参数存在主备制约，0：无主备制约关系，1:备机参数值需比主机大，2:主机参数值需比备机大
注意：此字段可能返回 null，表示取不到有效值。
        :type StandbyRelated: int
        :param VersionRelationSet: 参数版本关联信息，存储具体内核版本下的具体参数信息
注意：此字段可能返回 null，表示取不到有效值。
        :type VersionRelationSet: list of ParamVersionRelation
        :param SpecRelationSet: 参数规格关联信息，存储具体规格下具体的参数信息
注意：此字段可能返回 null，表示取不到有效值。
        :type SpecRelationSet: list of ParamSpecRelation
        """
        self.ID = None
        self.Name = None
        self.ParamValueType = None
        self.Unit = None
        self.DefaultValue = None
        self.CurrentValue = None
        self.Max = None
        self.EnumValue = None
        self.Min = None
        self.ParamDescriptionCH = None
        self.ParamDescriptionEN = None
        self.NeedReboot = None
        self.ClassificationCN = None
        self.ClassificationEN = None
        self.SpecRelated = None
        self.Advanced = None
        self.LastModifyTime = None
        self.StandbyRelated = None
        self.VersionRelationSet = None
        self.SpecRelationSet = None


    def _deserialize(self, params):
        self.ID = params.get("ID")
        self.Name = params.get("Name")
        self.ParamValueType = params.get("ParamValueType")
        self.Unit = params.get("Unit")
        self.DefaultValue = params.get("DefaultValue")
        self.CurrentValue = params.get("CurrentValue")
        self.Max = params.get("Max")
        self.EnumValue = params.get("EnumValue")
        self.Min = params.get("Min")
        self.ParamDescriptionCH = params.get("ParamDescriptionCH")
        self.ParamDescriptionEN = params.get("ParamDescriptionEN")
        self.NeedReboot = params.get("NeedReboot")
        self.ClassificationCN = params.get("ClassificationCN")
        self.ClassificationEN = params.get("ClassificationEN")
        self.SpecRelated = params.get("SpecRelated")
        self.Advanced = params.get("Advanced")
        self.LastModifyTime = params.get("LastModifyTime")
        self.StandbyRelated = params.get("StandbyRelated")
        if params.get("VersionRelationSet") is not None:
            self.VersionRelationSet = []
            for item in params.get("VersionRelationSet"):
                obj = ParamVersionRelation()
                obj._deserialize(item)
                self.VersionRelationSet.append(obj)
        if params.get("SpecRelationSet") is not None:
            self.SpecRelationSet = []
            for item in params.get("SpecRelationSet"):
                obj = ParamSpecRelation()
                obj._deserialize(item)
                self.SpecRelationSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ParamSpecRelation(AbstractModel):
    """描述各规格下的参数信息

    """

    def __init__(self):
        r"""
        :param Name: 参数名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param Memory: 参数信息所属规格
注意：此字段可能返回 null，表示取不到有效值。
        :type Memory: str
        :param Value: 参数在该规格下的默认值
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: str
        :param Unit: 参数值单位。参数没有单位时，该字段返回空
注意：此字段可能返回 null，表示取不到有效值。
        :type Unit: str
        :param Max: 数值类型（integer、real）参数，取值上界
注意：此字段可能返回 null，表示取不到有效值。
        :type Max: float
        :param Min: 数值类型（integer、real）参数，取值下界
注意：此字段可能返回 null，表示取不到有效值。
        :type Min: float
        :param EnumValue: 枚举类型参数，取值范围
注意：此字段可能返回 null，表示取不到有效值。
        :type EnumValue: list of str
        """
        self.Name = None
        self.Memory = None
        self.Value = None
        self.Unit = None
        self.Max = None
        self.Min = None
        self.EnumValue = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Memory = params.get("Memory")
        self.Value = params.get("Value")
        self.Unit = params.get("Unit")
        self.Max = params.get("Max")
        self.Min = params.get("Min")
        self.EnumValue = params.get("EnumValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ParamVersionRelation(AbstractModel):
    """描述各版本下的参数信息

    """

    def __init__(self):
        r"""
        :param Name: 参数名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param DBKernelVersion: 参数信息所属内核版本
注意：此字段可能返回 null，表示取不到有效值。
        :type DBKernelVersion: str
        :param Value: 参数在该版本该规格下的默认值
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: str
        :param Unit: 参数值单位。参数没有单位时，该字段返回空
注意：此字段可能返回 null，表示取不到有效值。
        :type Unit: str
        :param Max: 数值类型（integer、real）参数，取值上界
注意：此字段可能返回 null，表示取不到有效值。
        :type Max: float
        :param Min: 数值类型（integer、real）参数，取值下界
注意：此字段可能返回 null，表示取不到有效值。
        :type Min: float
        :param EnumValue: 枚举类型参数，取值范围
注意：此字段可能返回 null，表示取不到有效值。
        :type EnumValue: list of str
        """
        self.Name = None
        self.DBKernelVersion = None
        self.Value = None
        self.Unit = None
        self.Max = None
        self.Min = None
        self.EnumValue = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.DBKernelVersion = params.get("DBKernelVersion")
        self.Value = params.get("Value")
        self.Unit = params.get("Unit")
        self.Max = params.get("Max")
        self.Min = params.get("Min")
        self.EnumValue = params.get("EnumValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ParameterTemplate(AbstractModel):
    """参数模板的基本信息

    """

    def __init__(self):
        r"""
        :param TemplateId: 参数模板ID
        :type TemplateId: str
        :param TemplateName: 参数模板名称
        :type TemplateName: str
        :param DBMajorVersion: 参数模板适用的数据库版本
        :type DBMajorVersion: str
        :param DBEngine: 参数模板适用的数据库引擎
        :type DBEngine: str
        :param TemplateDescription: 参数模板描述
        :type TemplateDescription: str
        """
        self.TemplateId = None
        self.TemplateName = None
        self.DBMajorVersion = None
        self.DBEngine = None
        self.TemplateDescription = None


    def _deserialize(self, params):
        self.TemplateId = params.get("TemplateId")
        self.TemplateName = params.get("TemplateName")
        self.DBMajorVersion = params.get("DBMajorVersion")
        self.DBEngine = params.get("DBEngine")
        self.TemplateDescription = params.get("TemplateDescription")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PgDeal(AbstractModel):
    """订单详情

    """

    def __init__(self):
        r"""
        :param DealName: 订单名
        :type DealName: str
        :param OwnerUin: 所属用户
        :type OwnerUin: str
        :param Count: 订单涉及多少个实例
        :type Count: int
        :param PayMode: 付费模式。1-预付费；0-后付费
        :type PayMode: int
        :param FlowId: 异步任务流程ID
        :type FlowId: int
        :param DBInstanceIdSet: 实例ID数组
        :type DBInstanceIdSet: list of str
        """
        self.DealName = None
        self.OwnerUin = None
        self.Count = None
        self.PayMode = None
        self.FlowId = None
        self.DBInstanceIdSet = None


    def _deserialize(self, params):
        self.DealName = params.get("DealName")
        self.OwnerUin = params.get("OwnerUin")
        self.Count = params.get("Count")
        self.PayMode = params.get("PayMode")
        self.FlowId = params.get("FlowId")
        self.DBInstanceIdSet = params.get("DBInstanceIdSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PolicyRule(AbstractModel):
    """安全组规则信息

    """

    def __init__(self):
        r"""
        :param Action: 策略，ACCEPT 或者 DROP
        :type Action: str
        :param CidrIp: 来源或目的 IP 或 IP 段，例如172.16.0.0/12
        :type CidrIp: str
        :param PortRange: 端口
        :type PortRange: str
        :param IpProtocol: 网络协议，支持 UDP、TCP 等
        :type IpProtocol: str
        :param Description: 规则描述
        :type Description: str
        """
        self.Action = None
        self.CidrIp = None
        self.PortRange = None
        self.IpProtocol = None
        self.Description = None


    def _deserialize(self, params):
        self.Action = params.get("Action")
        self.CidrIp = params.get("CidrIp")
        self.PortRange = params.get("PortRange")
        self.IpProtocol = params.get("IpProtocol")
        self.Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RawSlowQuery(AbstractModel):
    """慢SQL查询接口返回 慢SQL列表详情

    """

    def __init__(self):
        r"""
        :param RawQuery: 慢SQL 语句
        :type RawQuery: str
        :param DatabaseName: 慢SQL 查询的数据库
        :type DatabaseName: str
        :param Duration: 慢SQL执行 耗时
        :type Duration: float
        :param ClientAddr: 执行慢SQL的客户端
        :type ClientAddr: str
        :param UserName: 执行慢SQL的用户名
        :type UserName: str
        :param SessionStartTime: 慢SQL执行的开始时间
        :type SessionStartTime: str
        """
        self.RawQuery = None
        self.DatabaseName = None
        self.Duration = None
        self.ClientAddr = None
        self.UserName = None
        self.SessionStartTime = None


    def _deserialize(self, params):
        self.RawQuery = params.get("RawQuery")
        self.DatabaseName = params.get("DatabaseName")
        self.Duration = params.get("Duration")
        self.ClientAddr = params.get("ClientAddr")
        self.UserName = params.get("UserName")
        self.SessionStartTime = params.get("SessionStartTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReadOnlyGroup(AbstractModel):
    """只读组信息

    """

    def __init__(self):
        r"""
        :param ReadOnlyGroupId: 只读组标识
注意：此字段可能返回 null，表示取不到有效值。
        :type ReadOnlyGroupId: str
        :param ReadOnlyGroupName: 只读组名字
注意：此字段可能返回 null，表示取不到有效值。
        :type ReadOnlyGroupName: str
        :param ProjectId: 项目id
注意：此字段可能返回 null，表示取不到有效值。
        :type ProjectId: int
        :param MasterDBInstanceId: 主实例id
注意：此字段可能返回 null，表示取不到有效值。
        :type MasterDBInstanceId: str
        :param MinDelayEliminateReserve: 最小保留实例数
注意：此字段可能返回 null，表示取不到有效值。
        :type MinDelayEliminateReserve: int
        :param MaxReplayLatency: 延迟空间大小阈值
        :type MaxReplayLatency: int
        :param ReplayLatencyEliminate: 延迟大小开关
        :type ReplayLatencyEliminate: int
        :param MaxReplayLag: 延迟时间大小阈值
        :type MaxReplayLag: float
        :param ReplayLagEliminate: 延迟时间开关
        :type ReplayLagEliminate: int
        :param VpcId: 虚拟网络id
        :type VpcId: str
        :param SubnetId: 子网id
注意：此字段可能返回 null，表示取不到有效值。
        :type SubnetId: str
        :param Region: 地域id
        :type Region: str
        :param Zone: 地区id
        :type Zone: str
        :param Status: 状态
        :type Status: str
        :param ReadOnlyDBInstanceList: 实例详细信息
        :type ReadOnlyDBInstanceList: list of DBInstance
        :param Rebalance: 自动负载均衡开关
        :type Rebalance: int
        :param DBInstanceNetInfo: 网络信息
        :type DBInstanceNetInfo: list of DBInstanceNetInfo
        :param NetworkAccessList: 只读组网络信息列表（此字段已废弃）
注意：此字段可能返回 null，表示取不到有效值。
        :type NetworkAccessList: list of NetworkAccess
        """
        self.ReadOnlyGroupId = None
        self.ReadOnlyGroupName = None
        self.ProjectId = None
        self.MasterDBInstanceId = None
        self.MinDelayEliminateReserve = None
        self.MaxReplayLatency = None
        self.ReplayLatencyEliminate = None
        self.MaxReplayLag = None
        self.ReplayLagEliminate = None
        self.VpcId = None
        self.SubnetId = None
        self.Region = None
        self.Zone = None
        self.Status = None
        self.ReadOnlyDBInstanceList = None
        self.Rebalance = None
        self.DBInstanceNetInfo = None
        self.NetworkAccessList = None


    def _deserialize(self, params):
        self.ReadOnlyGroupId = params.get("ReadOnlyGroupId")
        self.ReadOnlyGroupName = params.get("ReadOnlyGroupName")
        self.ProjectId = params.get("ProjectId")
        self.MasterDBInstanceId = params.get("MasterDBInstanceId")
        self.MinDelayEliminateReserve = params.get("MinDelayEliminateReserve")
        self.MaxReplayLatency = params.get("MaxReplayLatency")
        self.ReplayLatencyEliminate = params.get("ReplayLatencyEliminate")
        self.MaxReplayLag = params.get("MaxReplayLag")
        self.ReplayLagEliminate = params.get("ReplayLagEliminate")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.Region = params.get("Region")
        self.Zone = params.get("Zone")
        self.Status = params.get("Status")
        if params.get("ReadOnlyDBInstanceList") is not None:
            self.ReadOnlyDBInstanceList = []
            for item in params.get("ReadOnlyDBInstanceList"):
                obj = DBInstance()
                obj._deserialize(item)
                self.ReadOnlyDBInstanceList.append(obj)
        self.Rebalance = params.get("Rebalance")
        if params.get("DBInstanceNetInfo") is not None:
            self.DBInstanceNetInfo = []
            for item in params.get("DBInstanceNetInfo"):
                obj = DBInstanceNetInfo()
                obj._deserialize(item)
                self.DBInstanceNetInfo.append(obj)
        if params.get("NetworkAccessList") is not None:
            self.NetworkAccessList = []
            for item in params.get("NetworkAccessList"):
                obj = NetworkAccess()
                obj._deserialize(item)
                self.NetworkAccessList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RebalanceReadOnlyGroupRequest(AbstractModel):
    """RebalanceReadOnlyGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param ReadOnlyGroupId: 只读组ID
        :type ReadOnlyGroupId: str
        """
        self.ReadOnlyGroupId = None


    def _deserialize(self, params):
        self.ReadOnlyGroupId = params.get("ReadOnlyGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RebalanceReadOnlyGroupResponse(AbstractModel):
    """RebalanceReadOnlyGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class RegionInfo(AbstractModel):
    """描述地域的编码和状态等信息

    """

    def __init__(self):
        r"""
        :param Region: 该地域对应的英文名称
        :type Region: str
        :param RegionName: 该地域对应的中文名称
        :type RegionName: str
        :param RegionId: 该地域对应的数字编号
        :type RegionId: int
        :param RegionState: 可用状态，UNAVAILABLE表示不可用，AVAILABLE表示可用
        :type RegionState: str
        :param SupportInternational: 该地域是否支持国际站售卖，0：不支持，1：支持
注意：此字段可能返回 null，表示取不到有效值。
        :type SupportInternational: int
        """
        self.Region = None
        self.RegionName = None
        self.RegionId = None
        self.RegionState = None
        self.SupportInternational = None


    def _deserialize(self, params):
        self.Region = params.get("Region")
        self.RegionName = params.get("RegionName")
        self.RegionId = params.get("RegionId")
        self.RegionState = params.get("RegionState")
        self.SupportInternational = params.get("SupportInternational")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RemoveDBInstanceFromReadOnlyGroupRequest(AbstractModel):
    """RemoveDBInstanceFromReadOnlyGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param DBInstanceId: 实例ID
        :type DBInstanceId: str
        :param ReadOnlyGroupId: 只读组ID
        :type ReadOnlyGroupId: str
        """
        self.DBInstanceId = None
        self.ReadOnlyGroupId = None


    def _deserialize(self, params):
        self.DBInstanceId = params.get("DBInstanceId")
        self.ReadOnlyGroupId = params.get("ReadOnlyGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RemoveDBInstanceFromReadOnlyGroupResponse(AbstractModel):
    """RemoveDBInstanceFromReadOnlyGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param FlowId: 流程ID
        :type FlowId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.FlowId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        self.RequestId = params.get("RequestId")


class RenewInstanceRequest(AbstractModel):
    """RenewInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param DBInstanceId: 实例ID，形如postgres-6fego161
        :type DBInstanceId: str
        :param Period: 续费多少个月
        :type Period: int
        :param AutoVoucher: 是否自动使用代金券,1是,0否，默认不使用
        :type AutoVoucher: int
        :param VoucherIds: 代金券ID列表，目前仅支持指定一张代金券
        :type VoucherIds: list of str
        """
        self.DBInstanceId = None
        self.Period = None
        self.AutoVoucher = None
        self.VoucherIds = None


    def _deserialize(self, params):
        self.DBInstanceId = params.get("DBInstanceId")
        self.Period = params.get("Period")
        self.AutoVoucher = params.get("AutoVoucher")
        self.VoucherIds = params.get("VoucherIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RenewInstanceResponse(AbstractModel):
    """RenewInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param DealName: 订单名
        :type DealName: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DealName = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DealName = params.get("DealName")
        self.RequestId = params.get("RequestId")


class ResetAccountPasswordRequest(AbstractModel):
    """ResetAccountPassword请求参数结构体

    """

    def __init__(self):
        r"""
        :param DBInstanceId: 实例ID，形如postgres-4wdeb0zv
        :type DBInstanceId: str
        :param UserName: 实例账户名
        :type UserName: str
        :param Password: UserName账户对应的新密码
        :type Password: str
        """
        self.DBInstanceId = None
        self.UserName = None
        self.Password = None


    def _deserialize(self, params):
        self.DBInstanceId = params.get("DBInstanceId")
        self.UserName = params.get("UserName")
        self.Password = params.get("Password")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResetAccountPasswordResponse(AbstractModel):
    """ResetAccountPassword返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class RestartDBInstanceRequest(AbstractModel):
    """RestartDBInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param DBInstanceId: 实例ID，形如postgres-6r233v55
        :type DBInstanceId: str
        """
        self.DBInstanceId = None


    def _deserialize(self, params):
        self.DBInstanceId = params.get("DBInstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RestartDBInstanceResponse(AbstractModel):
    """RestartDBInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param FlowId: 异步流程ID
        :type FlowId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.FlowId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        self.RequestId = params.get("RequestId")


class SecurityGroup(AbstractModel):
    """安全组信息

    """

    def __init__(self):
        r"""
        :param ProjectId: 项目Id
        :type ProjectId: int
        :param CreateTime: 创建时间
        :type CreateTime: str
        :param Inbound: 入站规则
        :type Inbound: list of PolicyRule
        :param Outbound: 出站规则
        :type Outbound: list of PolicyRule
        :param SecurityGroupId: 安全组ID
        :type SecurityGroupId: str
        :param SecurityGroupName: 安全组名称
        :type SecurityGroupName: str
        :param SecurityGroupDescription: 安全组备注
        :type SecurityGroupDescription: str
        """
        self.ProjectId = None
        self.CreateTime = None
        self.Inbound = None
        self.Outbound = None
        self.SecurityGroupId = None
        self.SecurityGroupName = None
        self.SecurityGroupDescription = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.CreateTime = params.get("CreateTime")
        if params.get("Inbound") is not None:
            self.Inbound = []
            for item in params.get("Inbound"):
                obj = PolicyRule()
                obj._deserialize(item)
                self.Inbound.append(obj)
        if params.get("Outbound") is not None:
            self.Outbound = []
            for item in params.get("Outbound"):
                obj = PolicyRule()
                obj._deserialize(item)
                self.Outbound.append(obj)
        self.SecurityGroupId = params.get("SecurityGroupId")
        self.SecurityGroupName = params.get("SecurityGroupName")
        self.SecurityGroupDescription = params.get("SecurityGroupDescription")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ServerlessDBAccount(AbstractModel):
    """serverless账号描述

    """

    def __init__(self):
        r"""
        :param DBUser: 用户名
注意：此字段可能返回 null，表示取不到有效值。
        :type DBUser: str
        :param DBPassword: 密码
注意：此字段可能返回 null，表示取不到有效值。
        :type DBPassword: str
        :param DBConnLimit: 连接数限制
注意：此字段可能返回 null，表示取不到有效值。
        :type DBConnLimit: int
        """
        self.DBUser = None
        self.DBPassword = None
        self.DBConnLimit = None


    def _deserialize(self, params):
        self.DBUser = params.get("DBUser")
        self.DBPassword = params.get("DBPassword")
        self.DBConnLimit = params.get("DBConnLimit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ServerlessDBInstance(AbstractModel):
    """serverless实例描述

    """

    def __init__(self):
        r"""
        :param DBInstanceId: 实例id，唯一标识符
注意：此字段可能返回 null，表示取不到有效值。
        :type DBInstanceId: str
        :param DBInstanceName: 实例名称
注意：此字段可能返回 null，表示取不到有效值。
        :type DBInstanceName: str
        :param DBInstanceStatus: 实例状态
注意：此字段可能返回 null，表示取不到有效值。
        :type DBInstanceStatus: str
        :param Region: 地域
注意：此字段可能返回 null，表示取不到有效值。
        :type Region: str
        :param Zone: 可用区
注意：此字段可能返回 null，表示取不到有效值。
        :type Zone: str
        :param ProjectId: 项目id
注意：此字段可能返回 null，表示取不到有效值。
        :type ProjectId: int
        :param VpcId: 私有网络Id
注意：此字段可能返回 null，表示取不到有效值。
        :type VpcId: str
        :param SubnetId: 子网id
注意：此字段可能返回 null，表示取不到有效值。
        :type SubnetId: str
        :param DBCharset: 字符集
注意：此字段可能返回 null，表示取不到有效值。
        :type DBCharset: str
        :param DBVersion: 数据库版本
注意：此字段可能返回 null，表示取不到有效值。
        :type DBVersion: str
        :param CreateTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param DBInstanceNetInfo: 实例网络信息
注意：此字段可能返回 null，表示取不到有效值。
        :type DBInstanceNetInfo: list of ServerlessDBInstanceNetInfo
        :param DBAccountSet: 实例账户信息
注意：此字段可能返回 null，表示取不到有效值。
        :type DBAccountSet: list of ServerlessDBAccount
        :param DBDatabaseList: 实例下的db信息
注意：此字段可能返回 null，表示取不到有效值。
        :type DBDatabaseList: list of str
        :param TagList: 实例绑定的标签数组
注意：此字段可能返回 null，表示取不到有效值。
        :type TagList: list of Tag
        :param DBKernelVersion: 数据库内核版本
注意：此字段可能返回 null，表示取不到有效值。
        :type DBKernelVersion: str
        :param DBMajorVersion: 数据库主要版本
注意：此字段可能返回 null，表示取不到有效值。
        :type DBMajorVersion: str
        """
        self.DBInstanceId = None
        self.DBInstanceName = None
        self.DBInstanceStatus = None
        self.Region = None
        self.Zone = None
        self.ProjectId = None
        self.VpcId = None
        self.SubnetId = None
        self.DBCharset = None
        self.DBVersion = None
        self.CreateTime = None
        self.DBInstanceNetInfo = None
        self.DBAccountSet = None
        self.DBDatabaseList = None
        self.TagList = None
        self.DBKernelVersion = None
        self.DBMajorVersion = None


    def _deserialize(self, params):
        self.DBInstanceId = params.get("DBInstanceId")
        self.DBInstanceName = params.get("DBInstanceName")
        self.DBInstanceStatus = params.get("DBInstanceStatus")
        self.Region = params.get("Region")
        self.Zone = params.get("Zone")
        self.ProjectId = params.get("ProjectId")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.DBCharset = params.get("DBCharset")
        self.DBVersion = params.get("DBVersion")
        self.CreateTime = params.get("CreateTime")
        if params.get("DBInstanceNetInfo") is not None:
            self.DBInstanceNetInfo = []
            for item in params.get("DBInstanceNetInfo"):
                obj = ServerlessDBInstanceNetInfo()
                obj._deserialize(item)
                self.DBInstanceNetInfo.append(obj)
        if params.get("DBAccountSet") is not None:
            self.DBAccountSet = []
            for item in params.get("DBAccountSet"):
                obj = ServerlessDBAccount()
                obj._deserialize(item)
                self.DBAccountSet.append(obj)
        self.DBDatabaseList = params.get("DBDatabaseList")
        if params.get("TagList") is not None:
            self.TagList = []
            for item in params.get("TagList"):
                obj = Tag()
                obj._deserialize(item)
                self.TagList.append(obj)
        self.DBKernelVersion = params.get("DBKernelVersion")
        self.DBMajorVersion = params.get("DBMajorVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ServerlessDBInstanceNetInfo(AbstractModel):
    """serverless实例网络信息描述

    """

    def __init__(self):
        r"""
        :param Address: 地址
注意：此字段可能返回 null，表示取不到有效值。
        :type Address: str
        :param Ip: ip地址
注意：此字段可能返回 null，表示取不到有效值。
        :type Ip: str
        :param Port: 端口号
注意：此字段可能返回 null，表示取不到有效值。
        :type Port: int
        :param Status: 状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param NetType: 网络类型
注意：此字段可能返回 null，表示取不到有效值。
        :type NetType: str
        """
        self.Address = None
        self.Ip = None
        self.Port = None
        self.Status = None
        self.NetType = None


    def _deserialize(self, params):
        self.Address = params.get("Address")
        self.Ip = params.get("Ip")
        self.Port = params.get("Port")
        self.Status = params.get("Status")
        self.NetType = params.get("NetType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetAutoRenewFlagRequest(AbstractModel):
    """SetAutoRenewFlag请求参数结构体

    """

    def __init__(self):
        r"""
        :param DBInstanceIdSet: 实例ID集合。注意：当前已不支持同时操作多个实例，这里只能传入单个实例ID。
        :type DBInstanceIdSet: list of str
        :param AutoRenewFlag: 续费标记。0-正常续费；1-自动续费；2-到期不续费
        :type AutoRenewFlag: int
        """
        self.DBInstanceIdSet = None
        self.AutoRenewFlag = None


    def _deserialize(self, params):
        self.DBInstanceIdSet = params.get("DBInstanceIdSet")
        self.AutoRenewFlag = params.get("AutoRenewFlag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetAutoRenewFlagResponse(AbstractModel):
    """SetAutoRenewFlag返回参数结构体

    """

    def __init__(self):
        r"""
        :param Count: 设置成功的实例个数
        :type Count: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Count = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Count = params.get("Count")
        self.RequestId = params.get("RequestId")


class SlowlogDetail(AbstractModel):
    """慢查询详情

    """

    def __init__(self):
        r"""
        :param TotalTime: 花费总时间
        :type TotalTime: float
        :param TotalCalls: 调用总次数
        :type TotalCalls: int
        :param NormalQueries: 脱敏后的慢SQL列表
        :type NormalQueries: list of NormalQueryItem
        """
        self.TotalTime = None
        self.TotalCalls = None
        self.NormalQueries = None


    def _deserialize(self, params):
        self.TotalTime = params.get("TotalTime")
        self.TotalCalls = params.get("TotalCalls")
        if params.get("NormalQueries") is not None:
            self.NormalQueries = []
            for item in params.get("NormalQueries"):
                obj = NormalQueryItem()
                obj._deserialize(item)
                self.NormalQueries.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SpecInfo(AbstractModel):
    """描述某个地域下某个可用区的可售卖规格详细信息。

    """

    def __init__(self):
        r"""
        :param Region: 地域英文编码，对应RegionSet的Region字段
        :type Region: str
        :param Zone: 区域英文编码，对应ZoneSet的Zone字段
        :type Zone: str
        :param SpecItemInfoList: 规格详细信息列表
        :type SpecItemInfoList: list of SpecItemInfo
        :param SupportKMSRegions: 支持KMS的地域
注意：此字段可能返回 null，表示取不到有效值。
        :type SupportKMSRegions: list of str
        """
        self.Region = None
        self.Zone = None
        self.SpecItemInfoList = None
        self.SupportKMSRegions = None


    def _deserialize(self, params):
        self.Region = params.get("Region")
        self.Zone = params.get("Zone")
        if params.get("SpecItemInfoList") is not None:
            self.SpecItemInfoList = []
            for item in params.get("SpecItemInfoList"):
                obj = SpecItemInfo()
                obj._deserialize(item)
                self.SpecItemInfoList.append(obj)
        self.SupportKMSRegions = params.get("SupportKMSRegions")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SpecItemInfo(AbstractModel):
    """描述一种规格的信息

    """

    def __init__(self):
        r"""
        :param SpecCode: 规格ID
        :type SpecCode: str
        :param Version: PostgreSQL的版本编号
        :type Version: str
        :param VersionName: 内核编号对应的完整版本名称
        :type VersionName: str
        :param Cpu: CPU核数
        :type Cpu: int
        :param Memory: 内存大小，单位：MB
        :type Memory: int
        :param MaxStorage: 该规格所支持最大存储容量，单位：GB
        :type MaxStorage: int
        :param MinStorage: 该规格所支持最小存储容量，单位：GB
        :type MinStorage: int
        :param Qps: 该规格的预估QPS
        :type Qps: int
        :param Pid: 【该字段废弃】
        :type Pid: int
        :param Type: 机器类型
        :type Type: str
        :param MajorVersion: PostgreSQL的主要版本编号
注意：此字段可能返回 null，表示取不到有效值。
        :type MajorVersion: str
        :param KernelVersion: PostgreSQL的内核版本编号
注意：此字段可能返回 null，表示取不到有效值。
        :type KernelVersion: str
        :param IsSupportTDE: 是否支持TDE数据加密功能，0-不支持，1-支持
注意：此字段可能返回 null，表示取不到有效值。
        :type IsSupportTDE: int
        """
        self.SpecCode = None
        self.Version = None
        self.VersionName = None
        self.Cpu = None
        self.Memory = None
        self.MaxStorage = None
        self.MinStorage = None
        self.Qps = None
        self.Pid = None
        self.Type = None
        self.MajorVersion = None
        self.KernelVersion = None
        self.IsSupportTDE = None


    def _deserialize(self, params):
        self.SpecCode = params.get("SpecCode")
        self.Version = params.get("Version")
        self.VersionName = params.get("VersionName")
        self.Cpu = params.get("Cpu")
        self.Memory = params.get("Memory")
        self.MaxStorage = params.get("MaxStorage")
        self.MinStorage = params.get("MinStorage")
        self.Qps = params.get("Qps")
        self.Pid = params.get("Pid")
        self.Type = params.get("Type")
        self.MajorVersion = params.get("MajorVersion")
        self.KernelVersion = params.get("KernelVersion")
        self.IsSupportTDE = params.get("IsSupportTDE")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Tag(AbstractModel):
    """实例绑定的标签信息，包含标签键TagKey和标签值TagValue

    """

    def __init__(self):
        r"""
        :param TagKey: 标签键
        :type TagKey: str
        :param TagValue: 标签值
        :type TagValue: str
        """
        self.TagKey = None
        self.TagValue = None


    def _deserialize(self, params):
        self.TagKey = params.get("TagKey")
        self.TagValue = params.get("TagValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpgradeDBInstanceKernelVersionRequest(AbstractModel):
    """UpgradeDBInstanceKernelVersion请求参数结构体

    """

    def __init__(self):
        r"""
        :param DBInstanceId: 实例ID
        :type DBInstanceId: str
        :param TargetDBKernelVersion: 升级的目标内核版本号。可以通过接口DescribeDBVersions的返回字段AvailableUpgradeTarget获取。
        :type TargetDBKernelVersion: str
        :param SwitchTag: 指定实例升级内核版本号完成后的切换时间。可选值，
0：立即切换（默认值）。
1：指定时间切换。
2：维护时间窗口内切换。
        :type SwitchTag: int
        :param SwitchStartTime: 切换开始时间，时间格式：HH:MM:SS，例如：01:00:00。当SwitchTag为0或2时，该参数失效。
        :type SwitchStartTime: str
        :param SwitchEndTime: 切换截止时间，时间格式：HH:MM:SS，例如：01:30:00。当SwitchTag为0或2时，该参数失效。SwitchStartTime和SwitchEndTime时间窗口不能小于30分钟。
        :type SwitchEndTime: str
        :param DryRun: 是否对本次升级实例内核版本号操作执行预检查。可选值，
true：执行预检查操作，不升级内核版本号。检查项目包含请求参数、内核版本号兼容性、实例参数等。
false：发送正常请求（默认值），通过检查后直接升级内核版本号。
        :type DryRun: bool
        """
        self.DBInstanceId = None
        self.TargetDBKernelVersion = None
        self.SwitchTag = None
        self.SwitchStartTime = None
        self.SwitchEndTime = None
        self.DryRun = None


    def _deserialize(self, params):
        self.DBInstanceId = params.get("DBInstanceId")
        self.TargetDBKernelVersion = params.get("TargetDBKernelVersion")
        self.SwitchTag = params.get("SwitchTag")
        self.SwitchStartTime = params.get("SwitchStartTime")
        self.SwitchEndTime = params.get("SwitchEndTime")
        self.DryRun = params.get("DryRun")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpgradeDBInstanceKernelVersionResponse(AbstractModel):
    """UpgradeDBInstanceKernelVersion返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UpgradeDBInstanceRequest(AbstractModel):
    """UpgradeDBInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param Memory: 升级后的实例内存大小，单位GB
        :type Memory: int
        :param Storage: 升级后的实例磁盘大小，单位GB
        :type Storage: int
        :param DBInstanceId: 实例ID，形如postgres-lnp6j617
        :type DBInstanceId: str
        :param AutoVoucher: 是否自动使用代金券,1是,0否，默认不使用
        :type AutoVoucher: int
        :param VoucherIds: 代金券ID列表，目前仅支持指定一张代金券
        :type VoucherIds: list of str
        :param ActivityId: 活动ID
        :type ActivityId: int
        :param SwitchTag: 指定实例配置完成变更后的切换时间，默认为 立即切换，入参为 0 ：立即切换 。1：指定时间切换。
        :type SwitchTag: int
        :param SwitchStartTime: 切换开始时间
        :type SwitchStartTime: str
        :param SwitchEndTime: 切换截止时间
        :type SwitchEndTime: str
        """
        self.Memory = None
        self.Storage = None
        self.DBInstanceId = None
        self.AutoVoucher = None
        self.VoucherIds = None
        self.ActivityId = None
        self.SwitchTag = None
        self.SwitchStartTime = None
        self.SwitchEndTime = None


    def _deserialize(self, params):
        self.Memory = params.get("Memory")
        self.Storage = params.get("Storage")
        self.DBInstanceId = params.get("DBInstanceId")
        self.AutoVoucher = params.get("AutoVoucher")
        self.VoucherIds = params.get("VoucherIds")
        self.ActivityId = params.get("ActivityId")
        self.SwitchTag = params.get("SwitchTag")
        self.SwitchStartTime = params.get("SwitchStartTime")
        self.SwitchEndTime = params.get("SwitchEndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpgradeDBInstanceResponse(AbstractModel):
    """UpgradeDBInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param DealName: 交易名字。
        :type DealName: str
        :param BillId: 冻结流水号
        :type BillId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DealName = None
        self.BillId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DealName = params.get("DealName")
        self.BillId = params.get("BillId")
        self.RequestId = params.get("RequestId")


class Version(AbstractModel):
    """数据库版本号信息

    """

    def __init__(self):
        r"""
        :param DBEngine: 数据库引擎，支持：
1、postgresql（云数据库PostgreSQL）；
2、mssql_compatible（MSSQL兼容-云数据库PostgreSQL）；
        :type DBEngine: str
        :param DBVersion: 数据库版本，例如：12.4
        :type DBVersion: str
        :param DBMajorVersion: 数据库主要版本，例如：12
        :type DBMajorVersion: str
        :param DBKernelVersion: 数据库内核版本，例如：v12.4_r1.3
        :type DBKernelVersion: str
        :param SupportedFeatureNames: 数据库内核支持的特性列表。例如，
TDE：支持数据加密。
        :type SupportedFeatureNames: list of str
        :param Status: 数据库版本状态，包括：
AVAILABLE：可用；
DEPRECATED：已弃用。
        :type Status: str
        :param AvailableUpgradeTarget: 该数据库版本（DBKernelVersion）可以升级到的版本号列表。
        :type AvailableUpgradeTarget: list of str
        """
        self.DBEngine = None
        self.DBVersion = None
        self.DBMajorVersion = None
        self.DBKernelVersion = None
        self.SupportedFeatureNames = None
        self.Status = None
        self.AvailableUpgradeTarget = None


    def _deserialize(self, params):
        self.DBEngine = params.get("DBEngine")
        self.DBVersion = params.get("DBVersion")
        self.DBMajorVersion = params.get("DBMajorVersion")
        self.DBKernelVersion = params.get("DBKernelVersion")
        self.SupportedFeatureNames = params.get("SupportedFeatureNames")
        self.Status = params.get("Status")
        self.AvailableUpgradeTarget = params.get("AvailableUpgradeTarget")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Xlog(AbstractModel):
    """数据库Xlog信息

    """

    def __init__(self):
        r"""
        :param Id: 备份文件唯一标识
        :type Id: int
        :param StartTime: 文件生成的开始时间
        :type StartTime: str
        :param EndTime: 文件生成的结束时间
        :type EndTime: str
        :param InternalAddr: 内网下载地址
        :type InternalAddr: str
        :param ExternalAddr: 外网下载地址
        :type ExternalAddr: str
        :param Size: 备份文件大小
        :type Size: int
        """
        self.Id = None
        self.StartTime = None
        self.EndTime = None
        self.InternalAddr = None
        self.ExternalAddr = None
        self.Size = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.InternalAddr = params.get("InternalAddr")
        self.ExternalAddr = params.get("ExternalAddr")
        self.Size = params.get("Size")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ZoneInfo(AbstractModel):
    """描述可用区的编码和状态信息

    """

    def __init__(self):
        r"""
        :param Zone: 该可用区的英文名称
        :type Zone: str
        :param ZoneName: 该可用区的中文名称
        :type ZoneName: str
        :param ZoneId: 该可用区对应的数字编号
        :type ZoneId: int
        :param ZoneState: 可用状态包含，
UNAVAILABLE：不可用。
AVAILABLE：可用。
SELLOUT：售罄。
SUPPORTMODIFYONLY：支持变配。
        :type ZoneState: str
        :param ZoneSupportIpv6: 该可用区是否支持Ipv6
        :type ZoneSupportIpv6: int
        :param StandbyZoneSet: 该可用区对应的备可用区集合
注意：此字段可能返回 null，表示取不到有效值。
        :type StandbyZoneSet: list of str
        """
        self.Zone = None
        self.ZoneName = None
        self.ZoneId = None
        self.ZoneState = None
        self.ZoneSupportIpv6 = None
        self.StandbyZoneSet = None


    def _deserialize(self, params):
        self.Zone = params.get("Zone")
        self.ZoneName = params.get("ZoneName")
        self.ZoneId = params.get("ZoneId")
        self.ZoneState = params.get("ZoneState")
        self.ZoneSupportIpv6 = params.get("ZoneSupportIpv6")
        self.StandbyZoneSet = params.get("StandbyZoneSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        