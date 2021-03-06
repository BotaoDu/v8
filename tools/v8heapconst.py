# Copyright 2018 the V8 project authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can
# be found in the LICENSE file.

# This file is automatically generated by mkgrokdump and should not
# be modified manually.

# List of known V8 instance types.
INSTANCE_TYPES = {
  0: "INTERNALIZED_STRING_TYPE",
  2: "EXTERNAL_INTERNALIZED_STRING_TYPE",
  8: "ONE_BYTE_INTERNALIZED_STRING_TYPE",
  10: "EXTERNAL_ONE_BYTE_INTERNALIZED_STRING_TYPE",
  18: "EXTERNAL_INTERNALIZED_STRING_WITH_ONE_BYTE_DATA_TYPE",
  34: "UNCACHED_EXTERNAL_INTERNALIZED_STRING_TYPE",
  42: "UNCACHED_EXTERNAL_ONE_BYTE_INTERNALIZED_STRING_TYPE",
  50: "UNCACHED_EXTERNAL_INTERNALIZED_STRING_WITH_ONE_BYTE_DATA_TYPE",
  64: "STRING_TYPE",
  65: "CONS_STRING_TYPE",
  66: "EXTERNAL_STRING_TYPE",
  67: "SLICED_STRING_TYPE",
  69: "THIN_STRING_TYPE",
  72: "ONE_BYTE_STRING_TYPE",
  73: "CONS_ONE_BYTE_STRING_TYPE",
  74: "EXTERNAL_ONE_BYTE_STRING_TYPE",
  75: "SLICED_ONE_BYTE_STRING_TYPE",
  77: "THIN_ONE_BYTE_STRING_TYPE",
  82: "EXTERNAL_STRING_WITH_ONE_BYTE_DATA_TYPE",
  98: "UNCACHED_EXTERNAL_STRING_TYPE",
  106: "UNCACHED_EXTERNAL_ONE_BYTE_STRING_TYPE",
  114: "UNCACHED_EXTERNAL_STRING_WITH_ONE_BYTE_DATA_TYPE",
  128: "SYMBOL_TYPE",
  129: "HEAP_NUMBER_TYPE",
  130: "BIGINT_TYPE",
  131: "ODDBALL_TYPE",
  132: "MAP_TYPE",
  133: "CODE_TYPE",
  134: "MUTABLE_HEAP_NUMBER_TYPE",
  135: "FOREIGN_TYPE",
  136: "BYTE_ARRAY_TYPE",
  137: "BYTECODE_ARRAY_TYPE",
  138: "FREE_SPACE_TYPE",
  139: "FIXED_INT8_ARRAY_TYPE",
  140: "FIXED_UINT8_ARRAY_TYPE",
  141: "FIXED_INT16_ARRAY_TYPE",
  142: "FIXED_UINT16_ARRAY_TYPE",
  143: "FIXED_INT32_ARRAY_TYPE",
  144: "FIXED_UINT32_ARRAY_TYPE",
  145: "FIXED_FLOAT32_ARRAY_TYPE",
  146: "FIXED_FLOAT64_ARRAY_TYPE",
  147: "FIXED_UINT8_CLAMPED_ARRAY_TYPE",
  148: "FIXED_BIGINT64_ARRAY_TYPE",
  149: "FIXED_BIGUINT64_ARRAY_TYPE",
  150: "FIXED_DOUBLE_ARRAY_TYPE",
  151: "FEEDBACK_METADATA_TYPE",
  152: "FILLER_TYPE",
  153: "ACCESS_CHECK_INFO_TYPE",
  154: "ACCESSOR_INFO_TYPE",
  155: "ACCESSOR_PAIR_TYPE",
  156: "ALIASED_ARGUMENTS_ENTRY_TYPE",
  157: "ALLOCATION_MEMENTO_TYPE",
  158: "ASYNC_GENERATOR_REQUEST_TYPE",
  159: "DEBUG_INFO_TYPE",
  160: "FUNCTION_TEMPLATE_INFO_TYPE",
  161: "INTERCEPTOR_INFO_TYPE",
  162: "INTERPRETER_DATA_TYPE",
  163: "MODULE_INFO_ENTRY_TYPE",
  164: "MODULE_TYPE",
  165: "OBJECT_TEMPLATE_INFO_TYPE",
  166: "PROMISE_CAPABILITY_TYPE",
  167: "PROMISE_REACTION_TYPE",
  168: "PROTOTYPE_INFO_TYPE",
  169: "SCRIPT_TYPE",
  170: "STACK_FRAME_INFO_TYPE",
  171: "TUPLE2_TYPE",
  172: "TUPLE3_TYPE",
  173: "ARRAY_BOILERPLATE_DESCRIPTION_TYPE",
  174: "WASM_DEBUG_INFO_TYPE",
  175: "WASM_EXPORTED_FUNCTION_DATA_TYPE",
  176: "CALLABLE_TASK_TYPE",
  177: "CALLBACK_TASK_TYPE",
  178: "PROMISE_FULFILL_REACTION_JOB_TASK_TYPE",
  179: "PROMISE_REJECT_REACTION_JOB_TASK_TYPE",
  180: "PROMISE_RESOLVE_THENABLE_JOB_TASK_TYPE",
  181: "WEAK_FACTORY_CLEANUP_JOB_TASK_TYPE",
  182: "MICROTASK_QUEUE_TYPE",
  183: "ALLOCATION_SITE_TYPE",
  184: "FIXED_ARRAY_TYPE",
  185: "OBJECT_BOILERPLATE_DESCRIPTION_TYPE",
  186: "HASH_TABLE_TYPE",
  187: "ORDERED_HASH_MAP_TYPE",
  188: "ORDERED_HASH_SET_TYPE",
  189: "ORDERED_NAME_DICTIONARY_TYPE",
  190: "NAME_DICTIONARY_TYPE",
  191: "GLOBAL_DICTIONARY_TYPE",
  192: "NUMBER_DICTIONARY_TYPE",
  193: "SIMPLE_NUMBER_DICTIONARY_TYPE",
  194: "STRING_TABLE_TYPE",
  195: "EPHEMERON_HASH_TABLE_TYPE",
  196: "SCOPE_INFO_TYPE",
  197: "SCRIPT_CONTEXT_TABLE_TYPE",
  198: "AWAIT_CONTEXT_TYPE",
  199: "BLOCK_CONTEXT_TYPE",
  200: "CATCH_CONTEXT_TYPE",
  201: "DEBUG_EVALUATE_CONTEXT_TYPE",
  202: "EVAL_CONTEXT_TYPE",
  203: "FUNCTION_CONTEXT_TYPE",
  204: "MODULE_CONTEXT_TYPE",
  205: "NATIVE_CONTEXT_TYPE",
  206: "SCRIPT_CONTEXT_TYPE",
  207: "WITH_CONTEXT_TYPE",
  208: "WEAK_FIXED_ARRAY_TYPE",
  209: "DESCRIPTOR_ARRAY_TYPE",
  210: "TRANSITION_ARRAY_TYPE",
  211: "CALL_HANDLER_INFO_TYPE",
  212: "CELL_TYPE",
  213: "CODE_DATA_CONTAINER_TYPE",
  214: "FEEDBACK_CELL_TYPE",
  215: "FEEDBACK_VECTOR_TYPE",
  216: "LOAD_HANDLER_TYPE",
  217: "PRE_PARSED_SCOPE_DATA_TYPE",
  218: "PROPERTY_ARRAY_TYPE",
  219: "PROPERTY_CELL_TYPE",
  220: "SHARED_FUNCTION_INFO_TYPE",
  221: "SMALL_ORDERED_HASH_MAP_TYPE",
  222: "SMALL_ORDERED_HASH_SET_TYPE",
  223: "STORE_HANDLER_TYPE",
  224: "UNCOMPILED_DATA_WITHOUT_PRE_PARSED_SCOPE_TYPE",
  225: "UNCOMPILED_DATA_WITH_PRE_PARSED_SCOPE_TYPE",
  226: "WEAK_ARRAY_LIST_TYPE",
  1024: "JS_PROXY_TYPE",
  1025: "JS_GLOBAL_OBJECT_TYPE",
  1026: "JS_GLOBAL_PROXY_TYPE",
  1027: "JS_MODULE_NAMESPACE_TYPE",
  1040: "JS_SPECIAL_API_OBJECT_TYPE",
  1041: "JS_VALUE_TYPE",
  1056: "JS_API_OBJECT_TYPE",
  1057: "JS_OBJECT_TYPE",
  1058: "JS_ARGUMENTS_TYPE",
  1059: "JS_ARRAY_BUFFER_TYPE",
  1060: "JS_ARRAY_ITERATOR_TYPE",
  1061: "JS_ARRAY_TYPE",
  1062: "JS_ASYNC_FROM_SYNC_ITERATOR_TYPE",
  1063: "JS_ASYNC_FUNCTION_OBJECT_TYPE",
  1064: "JS_ASYNC_GENERATOR_OBJECT_TYPE",
  1065: "JS_CONTEXT_EXTENSION_OBJECT_TYPE",
  1066: "JS_DATE_TYPE",
  1067: "JS_ERROR_TYPE",
  1068: "JS_GENERATOR_OBJECT_TYPE",
  1069: "JS_MAP_TYPE",
  1070: "JS_MAP_KEY_ITERATOR_TYPE",
  1071: "JS_MAP_KEY_VALUE_ITERATOR_TYPE",
  1072: "JS_MAP_VALUE_ITERATOR_TYPE",
  1073: "JS_MESSAGE_OBJECT_TYPE",
  1074: "JS_PROMISE_TYPE",
  1075: "JS_REGEXP_TYPE",
  1076: "JS_REGEXP_STRING_ITERATOR_TYPE",
  1077: "JS_SET_TYPE",
  1078: "JS_SET_KEY_VALUE_ITERATOR_TYPE",
  1079: "JS_SET_VALUE_ITERATOR_TYPE",
  1080: "JS_STRING_ITERATOR_TYPE",
  1081: "JS_WEAK_CELL_TYPE",
  1082: "JS_WEAK_REF_TYPE",
  1083: "JS_WEAK_FACTORY_CLEANUP_ITERATOR_TYPE",
  1084: "JS_WEAK_FACTORY_TYPE",
  1085: "JS_WEAK_MAP_TYPE",
  1086: "JS_WEAK_SET_TYPE",
  1087: "JS_TYPED_ARRAY_TYPE",
  1088: "JS_DATA_VIEW_TYPE",
  1089: "JS_INTL_V8_BREAK_ITERATOR_TYPE",
  1090: "JS_INTL_COLLATOR_TYPE",
  1091: "JS_INTL_DATE_TIME_FORMAT_TYPE",
  1092: "JS_INTL_LIST_FORMAT_TYPE",
  1093: "JS_INTL_LOCALE_TYPE",
  1094: "JS_INTL_NUMBER_FORMAT_TYPE",
  1095: "JS_INTL_PLURAL_RULES_TYPE",
  1096: "JS_INTL_RELATIVE_TIME_FORMAT_TYPE",
  1097: "JS_INTL_SEGMENT_ITERATOR_TYPE",
  1098: "JS_INTL_SEGMENTER_TYPE",
  1099: "WASM_EXCEPTION_TYPE",
  1100: "WASM_GLOBAL_TYPE",
  1101: "WASM_INSTANCE_TYPE",
  1102: "WASM_MEMORY_TYPE",
  1103: "WASM_MODULE_TYPE",
  1104: "WASM_TABLE_TYPE",
  1105: "JS_BOUND_FUNCTION_TYPE",
  1106: "JS_FUNCTION_TYPE",
}

# List of known V8 maps.
KNOWN_MAPS = {
  ("RO_SPACE", 0x00139): (138, "FreeSpaceMap"),
  ("RO_SPACE", 0x00189): (132, "MetaMap"),
  ("RO_SPACE", 0x00209): (131, "NullMap"),
  ("RO_SPACE", 0x00279): (209, "DescriptorArrayMap"),
  ("RO_SPACE", 0x002d9): (208, "WeakFixedArrayMap"),
  ("RO_SPACE", 0x00329): (152, "OnePointerFillerMap"),
  ("RO_SPACE", 0x00379): (152, "TwoPointerFillerMap"),
  ("RO_SPACE", 0x003f9): (131, "UninitializedMap"),
  ("RO_SPACE", 0x00469): (8, "OneByteInternalizedStringMap"),
  ("RO_SPACE", 0x00509): (131, "UndefinedMap"),
  ("RO_SPACE", 0x00569): (129, "HeapNumberMap"),
  ("RO_SPACE", 0x005e9): (131, "TheHoleMap"),
  ("RO_SPACE", 0x00691): (131, "BooleanMap"),
  ("RO_SPACE", 0x00769): (136, "ByteArrayMap"),
  ("RO_SPACE", 0x007b9): (184, "FixedArrayMap"),
  ("RO_SPACE", 0x00809): (184, "FixedCOWArrayMap"),
  ("RO_SPACE", 0x00859): (186, "HashTableMap"),
  ("RO_SPACE", 0x008a9): (128, "SymbolMap"),
  ("RO_SPACE", 0x008f9): (72, "OneByteStringMap"),
  ("RO_SPACE", 0x00949): (196, "ScopeInfoMap"),
  ("RO_SPACE", 0x00999): (220, "SharedFunctionInfoMap"),
  ("RO_SPACE", 0x009e9): (133, "CodeMap"),
  ("RO_SPACE", 0x00a39): (203, "FunctionContextMap"),
  ("RO_SPACE", 0x00a89): (212, "CellMap"),
  ("RO_SPACE", 0x00ad9): (219, "GlobalPropertyCellMap"),
  ("RO_SPACE", 0x00b29): (135, "ForeignMap"),
  ("RO_SPACE", 0x00b79): (210, "TransitionArrayMap"),
  ("RO_SPACE", 0x00bc9): (215, "FeedbackVectorMap"),
  ("RO_SPACE", 0x00c69): (131, "ArgumentsMarkerMap"),
  ("RO_SPACE", 0x00d09): (131, "ExceptionMap"),
  ("RO_SPACE", 0x00da9): (131, "TerminationExceptionMap"),
  ("RO_SPACE", 0x00e51): (131, "OptimizedOutMap"),
  ("RO_SPACE", 0x00ef1): (131, "StaleRegisterMap"),
  ("RO_SPACE", 0x00f61): (205, "NativeContextMap"),
  ("RO_SPACE", 0x00fb1): (204, "ModuleContextMap"),
  ("RO_SPACE", 0x01001): (202, "EvalContextMap"),
  ("RO_SPACE", 0x01051): (206, "ScriptContextMap"),
  ("RO_SPACE", 0x010a1): (198, "AwaitContextMap"),
  ("RO_SPACE", 0x010f1): (199, "BlockContextMap"),
  ("RO_SPACE", 0x01141): (200, "CatchContextMap"),
  ("RO_SPACE", 0x01191): (207, "WithContextMap"),
  ("RO_SPACE", 0x011e1): (201, "DebugEvaluateContextMap"),
  ("RO_SPACE", 0x01231): (197, "ScriptContextTableMap"),
  ("RO_SPACE", 0x01281): (151, "FeedbackMetadataArrayMap"),
  ("RO_SPACE", 0x012d1): (184, "ArrayListMap"),
  ("RO_SPACE", 0x01321): (130, "BigIntMap"),
  ("RO_SPACE", 0x01371): (185, "ObjectBoilerplateDescriptionMap"),
  ("RO_SPACE", 0x013c1): (137, "BytecodeArrayMap"),
  ("RO_SPACE", 0x01411): (213, "CodeDataContainerMap"),
  ("RO_SPACE", 0x01461): (150, "FixedDoubleArrayMap"),
  ("RO_SPACE", 0x014b1): (191, "GlobalDictionaryMap"),
  ("RO_SPACE", 0x01501): (214, "ManyClosuresCellMap"),
  ("RO_SPACE", 0x01551): (184, "ModuleInfoMap"),
  ("RO_SPACE", 0x015a1): (134, "MutableHeapNumberMap"),
  ("RO_SPACE", 0x015f1): (190, "NameDictionaryMap"),
  ("RO_SPACE", 0x01641): (214, "NoClosuresCellMap"),
  ("RO_SPACE", 0x01691): (192, "NumberDictionaryMap"),
  ("RO_SPACE", 0x016e1): (214, "OneClosureCellMap"),
  ("RO_SPACE", 0x01731): (187, "OrderedHashMapMap"),
  ("RO_SPACE", 0x01781): (188, "OrderedHashSetMap"),
  ("RO_SPACE", 0x017d1): (189, "OrderedNameDictionaryMap"),
  ("RO_SPACE", 0x01821): (217, "PreParsedScopeDataMap"),
  ("RO_SPACE", 0x01871): (218, "PropertyArrayMap"),
  ("RO_SPACE", 0x018c1): (211, "SideEffectCallHandlerInfoMap"),
  ("RO_SPACE", 0x01911): (211, "SideEffectFreeCallHandlerInfoMap"),
  ("RO_SPACE", 0x01961): (211, "NextCallSideEffectFreeCallHandlerInfoMap"),
  ("RO_SPACE", 0x019b1): (193, "SimpleNumberDictionaryMap"),
  ("RO_SPACE", 0x01a01): (184, "SloppyArgumentsElementsMap"),
  ("RO_SPACE", 0x01a51): (221, "SmallOrderedHashMapMap"),
  ("RO_SPACE", 0x01aa1): (222, "SmallOrderedHashSetMap"),
  ("RO_SPACE", 0x01af1): (194, "StringTableMap"),
  ("RO_SPACE", 0x01b41): (224, "UncompiledDataWithoutPreParsedScopeMap"),
  ("RO_SPACE", 0x01b91): (225, "UncompiledDataWithPreParsedScopeMap"),
  ("RO_SPACE", 0x01be1): (226, "WeakArrayListMap"),
  ("RO_SPACE", 0x01c31): (195, "EphemeronHashTableMap"),
  ("RO_SPACE", 0x01c81): (106, "NativeSourceStringMap"),
  ("RO_SPACE", 0x01cd1): (64, "StringMap"),
  ("RO_SPACE", 0x01d21): (73, "ConsOneByteStringMap"),
  ("RO_SPACE", 0x01d71): (65, "ConsStringMap"),
  ("RO_SPACE", 0x01dc1): (77, "ThinOneByteStringMap"),
  ("RO_SPACE", 0x01e11): (69, "ThinStringMap"),
  ("RO_SPACE", 0x01e61): (67, "SlicedStringMap"),
  ("RO_SPACE", 0x01eb1): (75, "SlicedOneByteStringMap"),
  ("RO_SPACE", 0x01f01): (66, "ExternalStringMap"),
  ("RO_SPACE", 0x01f51): (82, "ExternalStringWithOneByteDataMap"),
  ("RO_SPACE", 0x01fa1): (74, "ExternalOneByteStringMap"),
  ("RO_SPACE", 0x01ff1): (98, "UncachedExternalStringMap"),
  ("RO_SPACE", 0x02041): (114, "UncachedExternalStringWithOneByteDataMap"),
  ("RO_SPACE", 0x02091): (0, "InternalizedStringMap"),
  ("RO_SPACE", 0x020e1): (2, "ExternalInternalizedStringMap"),
  ("RO_SPACE", 0x02131): (18, "ExternalInternalizedStringWithOneByteDataMap"),
  ("RO_SPACE", 0x02181): (10, "ExternalOneByteInternalizedStringMap"),
  ("RO_SPACE", 0x021d1): (34, "UncachedExternalInternalizedStringMap"),
  ("RO_SPACE", 0x02221): (50, "UncachedExternalInternalizedStringWithOneByteDataMap"),
  ("RO_SPACE", 0x02271): (42, "UncachedExternalOneByteInternalizedStringMap"),
  ("RO_SPACE", 0x022c1): (106, "UncachedExternalOneByteStringMap"),
  ("RO_SPACE", 0x02311): (140, "FixedUint8ArrayMap"),
  ("RO_SPACE", 0x02361): (139, "FixedInt8ArrayMap"),
  ("RO_SPACE", 0x023b1): (142, "FixedUint16ArrayMap"),
  ("RO_SPACE", 0x02401): (141, "FixedInt16ArrayMap"),
  ("RO_SPACE", 0x02451): (144, "FixedUint32ArrayMap"),
  ("RO_SPACE", 0x024a1): (143, "FixedInt32ArrayMap"),
  ("RO_SPACE", 0x024f1): (145, "FixedFloat32ArrayMap"),
  ("RO_SPACE", 0x02541): (146, "FixedFloat64ArrayMap"),
  ("RO_SPACE", 0x02591): (147, "FixedUint8ClampedArrayMap"),
  ("RO_SPACE", 0x025e1): (149, "FixedBigUint64ArrayMap"),
  ("RO_SPACE", 0x02631): (148, "FixedBigInt64ArrayMap"),
  ("RO_SPACE", 0x02681): (131, "SelfReferenceMarkerMap"),
  ("RO_SPACE", 0x026e9): (171, "Tuple2Map"),
  ("RO_SPACE", 0x02789): (173, "ArrayBoilerplateDescriptionMap"),
  ("RO_SPACE", 0x02ac9): (161, "InterceptorInfoMap"),
  ("RO_SPACE", 0x04f51): (153, "AccessCheckInfoMap"),
  ("RO_SPACE", 0x04fa1): (154, "AccessorInfoMap"),
  ("RO_SPACE", 0x04ff1): (155, "AccessorPairMap"),
  ("RO_SPACE", 0x05041): (156, "AliasedArgumentsEntryMap"),
  ("RO_SPACE", 0x05091): (157, "AllocationMementoMap"),
  ("RO_SPACE", 0x050e1): (158, "AsyncGeneratorRequestMap"),
  ("RO_SPACE", 0x05131): (159, "DebugInfoMap"),
  ("RO_SPACE", 0x05181): (160, "FunctionTemplateInfoMap"),
  ("RO_SPACE", 0x051d1): (162, "InterpreterDataMap"),
  ("RO_SPACE", 0x05221): (163, "ModuleInfoEntryMap"),
  ("RO_SPACE", 0x05271): (164, "ModuleMap"),
  ("RO_SPACE", 0x052c1): (165, "ObjectTemplateInfoMap"),
  ("RO_SPACE", 0x05311): (166, "PromiseCapabilityMap"),
  ("RO_SPACE", 0x05361): (167, "PromiseReactionMap"),
  ("RO_SPACE", 0x053b1): (168, "PrototypeInfoMap"),
  ("RO_SPACE", 0x05401): (169, "ScriptMap"),
  ("RO_SPACE", 0x05451): (170, "StackFrameInfoMap"),
  ("RO_SPACE", 0x054a1): (172, "Tuple3Map"),
  ("RO_SPACE", 0x054f1): (174, "WasmDebugInfoMap"),
  ("RO_SPACE", 0x05541): (175, "WasmExportedFunctionDataMap"),
  ("RO_SPACE", 0x05591): (176, "CallableTaskMap"),
  ("RO_SPACE", 0x055e1): (177, "CallbackTaskMap"),
  ("RO_SPACE", 0x05631): (178, "PromiseFulfillReactionJobTaskMap"),
  ("RO_SPACE", 0x05681): (179, "PromiseRejectReactionJobTaskMap"),
  ("RO_SPACE", 0x056d1): (180, "PromiseResolveThenableJobTaskMap"),
  ("RO_SPACE", 0x05721): (181, "WeakFactoryCleanupJobTaskMap"),
  ("RO_SPACE", 0x05771): (182, "MicrotaskQueueMap"),
  ("RO_SPACE", 0x057c1): (183, "AllocationSiteWithWeakNextMap"),
  ("RO_SPACE", 0x05811): (183, "AllocationSiteWithoutWeakNextMap"),
  ("RO_SPACE", 0x05861): (216, "LoadHandler1Map"),
  ("RO_SPACE", 0x058b1): (216, "LoadHandler2Map"),
  ("RO_SPACE", 0x05901): (216, "LoadHandler3Map"),
  ("RO_SPACE", 0x05951): (223, "StoreHandler0Map"),
  ("RO_SPACE", 0x059a1): (223, "StoreHandler1Map"),
  ("RO_SPACE", 0x059f1): (223, "StoreHandler2Map"),
  ("RO_SPACE", 0x05a41): (223, "StoreHandler3Map"),
  ("MAP_SPACE", 0x00139): (1057, "ExternalMap"),
  ("MAP_SPACE", 0x00189): (1073, "JSMessageObjectMap"),
}

# List of known V8 objects.
KNOWN_OBJECTS = {
  ("RO_SPACE", 0x001d9): "NullValue",
  ("RO_SPACE", 0x00259): "EmptyDescriptorArray",
  ("RO_SPACE", 0x002c9): "EmptyWeakFixedArray",
  ("RO_SPACE", 0x003c9): "UninitializedValue",
  ("RO_SPACE", 0x004d9): "UndefinedValue",
  ("RO_SPACE", 0x00559): "NanValue",
  ("RO_SPACE", 0x005b9): "TheHoleValue",
  ("RO_SPACE", 0x00651): "HoleNanValue",
  ("RO_SPACE", 0x00661): "TrueValue",
  ("RO_SPACE", 0x00711): "FalseValue",
  ("RO_SPACE", 0x00759): "empty_string",
  ("RO_SPACE", 0x00c19): "EmptyScopeInfo",
  ("RO_SPACE", 0x00c29): "EmptyFixedArray",
  ("RO_SPACE", 0x00c39): "ArgumentsMarker",
  ("RO_SPACE", 0x00cd9): "Exception",
  ("RO_SPACE", 0x00d79): "TerminationException",
  ("RO_SPACE", 0x00e21): "OptimizedOut",
  ("RO_SPACE", 0x00ec1): "StaleRegister",
  ("RO_SPACE", 0x026d1): "EmptyEnumCache",
  ("RO_SPACE", 0x02739): "EmptyPropertyArray",
  ("RO_SPACE", 0x02749): "EmptyByteArray",
  ("RO_SPACE", 0x02759): "EmptyObjectBoilerplateDescription",
  ("RO_SPACE", 0x02771): "EmptyArrayBoilerplateDescription",
  ("RO_SPACE", 0x027d9): "EmptyFixedUint8Array",
  ("RO_SPACE", 0x027f9): "EmptyFixedInt8Array",
  ("RO_SPACE", 0x02819): "EmptyFixedUint16Array",
  ("RO_SPACE", 0x02839): "EmptyFixedInt16Array",
  ("RO_SPACE", 0x02859): "EmptyFixedUint32Array",
  ("RO_SPACE", 0x02879): "EmptyFixedInt32Array",
  ("RO_SPACE", 0x02899): "EmptyFixedFloat32Array",
  ("RO_SPACE", 0x028b9): "EmptyFixedFloat64Array",
  ("RO_SPACE", 0x028d9): "EmptyFixedUint8ClampedArray",
  ("RO_SPACE", 0x028f9): "EmptyFixedBigUint64Array",
  ("RO_SPACE", 0x02919): "EmptyFixedBigInt64Array",
  ("RO_SPACE", 0x02939): "EmptySloppyArgumentsElements",
  ("RO_SPACE", 0x02959): "EmptySlowElementDictionary",
  ("RO_SPACE", 0x029a1): "EmptyOrderedHashMap",
  ("RO_SPACE", 0x029c9): "EmptyOrderedHashSet",
  ("RO_SPACE", 0x029f1): "EmptyFeedbackMetadata",
  ("RO_SPACE", 0x02a01): "EmptyPropertyCell",
  ("RO_SPACE", 0x02a29): "EmptyPropertyDictionary",
  ("RO_SPACE", 0x02a79): "NoOpInterceptorInfo",
  ("RO_SPACE", 0x02b19): "EmptyWeakArrayList",
  ("RO_SPACE", 0x02b31): "InfinityValue",
  ("RO_SPACE", 0x02b41): "MinusZeroValue",
  ("RO_SPACE", 0x02b51): "MinusInfinityValue",
  ("RO_SPACE", 0x02b61): "SelfReferenceMarker",
  ("RO_SPACE", 0x02bb9): "OffHeapTrampolineRelocationInfo",
  ("RO_SPACE", 0x02bd1): "HashSeed",
  ("OLD_SPACE", 0x00139): "ArgumentsIteratorAccessor",
  ("OLD_SPACE", 0x001a9): "ArrayLengthAccessor",
  ("OLD_SPACE", 0x00219): "BoundFunctionLengthAccessor",
  ("OLD_SPACE", 0x00289): "BoundFunctionNameAccessor",
  ("OLD_SPACE", 0x002f9): "ErrorStackAccessor",
  ("OLD_SPACE", 0x00369): "FunctionArgumentsAccessor",
  ("OLD_SPACE", 0x003d9): "FunctionCallerAccessor",
  ("OLD_SPACE", 0x00449): "FunctionNameAccessor",
  ("OLD_SPACE", 0x004b9): "FunctionLengthAccessor",
  ("OLD_SPACE", 0x00529): "FunctionPrototypeAccessor",
  ("OLD_SPACE", 0x00599): "StringLengthAccessor",
  ("OLD_SPACE", 0x00609): "InvalidPrototypeValidityCell",
  ("OLD_SPACE", 0x00619): "EmptyScript",
  ("OLD_SPACE", 0x00699): "ManyClosuresCell",
  ("OLD_SPACE", 0x006a9): "ArrayConstructorProtector",
  ("OLD_SPACE", 0x006b9): "NoElementsProtector",
  ("OLD_SPACE", 0x006e1): "IsConcatSpreadableProtector",
  ("OLD_SPACE", 0x006f1): "ArraySpeciesProtector",
  ("OLD_SPACE", 0x00719): "TypedArraySpeciesProtector",
  ("OLD_SPACE", 0x00741): "PromiseSpeciesProtector",
  ("OLD_SPACE", 0x00769): "StringLengthProtector",
  ("OLD_SPACE", 0x00779): "ArrayIteratorProtector",
  ("OLD_SPACE", 0x007a1): "ArrayBufferNeuteringProtector",
  ("OLD_SPACE", 0x007c9): "PromiseHookProtector",
  ("OLD_SPACE", 0x007f1): "PromiseResolveProtector",
  ("OLD_SPACE", 0x00801): "MapIteratorProtector",
  ("OLD_SPACE", 0x00829): "PromiseThenProtector",
  ("OLD_SPACE", 0x00851): "SetIteratorProtector",
  ("OLD_SPACE", 0x00879): "StringIteratorProtector",
  ("OLD_SPACE", 0x008a1): "SingleCharacterStringCache",
  ("OLD_SPACE", 0x010b1): "StringSplitCache",
  ("OLD_SPACE", 0x018c1): "RegExpMultipleCache",
  ("OLD_SPACE", 0x020d1): "DefaultMicrotaskQueue",
  ("OLD_SPACE", 0x020e9): "BuiltinsConstantsTable",
}

# List of known V8 Frame Markers.
FRAME_MARKERS = (
  "ENTRY",
  "CONSTRUCT_ENTRY",
  "EXIT",
  "OPTIMIZED",
  "WASM_COMPILED",
  "WASM_TO_JS",
  "JS_TO_WASM",
  "WASM_INTERPRETER_ENTRY",
  "C_WASM_ENTRY",
  "WASM_COMPILE_LAZY",
  "INTERPRETED",
  "STUB",
  "BUILTIN_CONTINUATION",
  "JAVA_SCRIPT_BUILTIN_CONTINUATION",
  "JAVA_SCRIPT_BUILTIN_CONTINUATION_WITH_CATCH",
  "INTERNAL",
  "CONSTRUCT",
  "ARGUMENTS_ADAPTOR",
  "BUILTIN",
  "BUILTIN_EXIT",
  "NATIVE",
)

# This set of constants is generated from a shipping build.
